from django.shortcuts import get_object_or_404
from .permissions import IsAuthorOrReadOnly
from question.models import Answer, Question
from rest_framework import generics
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import AnswerSerializer, QuestionSerializer


class QuestionAPIModelView(ModelViewSet):
    """ list,retrive,delete,post per un'istanza di Question """

    queryset = Question.objects.all().order_by("-created_at")
    serializer_class = QuestionSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        """ collego automaticamente l'autore della domanda ad essa stessa """
        serializer.save(author=self.request.user)


class AnswerCreateAPIView(generics.CreateAPIView):
    """ create an instance of Answer """

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """ controllo che l'utente non abbiamo già risposto;
            collego automaticamente la risposta all'utente e alla domanda """
        slug = self.kwargs.get('slug')
        user = self.request.user
        question = get_object_or_404(Question, slug=slug)

        if question.answers.filter(author=user).exists():
            raise ValidationError("Hai già risposto a questa domanda!")
        serializer.save(author=user, question=question)


class AnswersListAPIView(generics.ListAPIView):
    """ lista di risposte per una sola domanda """

    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """ sovrascrivo il metodo e non uso 'queryset' perchè voglio le risposte 
            di una sola domanda, non tutte le risposte in tutto il Database """

        slug = self.kwargs.get('slug')
        return Answer.objects.filter(question__slug=slug).order_by("-created_at")


class AnswerRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    """ Retrive, Update, Delete un'istanza di Answer """

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class AnswerLikeAPIView(APIView):
    """ mette o toglie un 'like' alla risposta """

    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        """ like """
        user = self.request.user
        answer = get_object_or_404(Answer, pk=pk)

        answer.voters.add(user)

        context = { "request": request}
        serializer = self.serializer_class(answer, context=context)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def delete(self, request, pk):
        """ unlike """
        user = self.request.user
        answer = get_object_or_404(Answer, pk=pk)

        answer.voters.remove(user)

        context = { "request": request }
        serializer = self.serializer_class(answer, context=context)

        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
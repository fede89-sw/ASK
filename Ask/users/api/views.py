from rest_framework import generics
from .serializers import CustomUserSerializer


class LoggedUsername(generics.RetrieveAPIView):
    """ ottengo lo username dello user loggato """
    serializer_class = CustomUserSerializer

    def get_object(self):
        """ sovrascrivo metodo per ottenere l'oggetto senza aver bisogno di pk 
            o parametri passati alla funzione """
        return self.request.user
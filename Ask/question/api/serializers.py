from rest_framework import serializers
from question.models import Answer, Question

import locale
locale.setlocale(locale.LC_TIME, 'Italian_Italy')

class AnswerSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)
    user_has_voted = serializers.SerializerMethodField(read_only=True)

    class Meta():
        model = Answer
        exclude = ["updated_at", "question", "voters"]

    def get_created_at(self, instance):
        """ voglio la data in formato italiano """
        return instance.created_at.strftime('%d %B %Y')

    def get_likes_count(self, instance):
        """ numero likes per una risposta """
        return instance.voters.count()

    def get_user_has_voted(self, instance):
        """ true o false se l'user ha messo like """
        request = self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()


class QuestionSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    answer_count = serializers.SerializerMethodField(read_only=True)
    user_has_answered = serializers.SerializerMethodField(read_only=True)

    class Meta():
        model = Question
        exclude = ["updated_at"]

    def get_created_at(self, instance):
        """ voglio la data in formato italiano """
        return instance.created_at.strftime('%d %B %Y')

    def get_answer_count(self, instance):
        """ numero likes per una risposta """
        return instance.answers.count()

    def get_user_has_answered(self, instance):
        """ true o false se l'user ha messo like """
        request = self.context.get("request")
        return instance.answers.filter(author=request.user).exists()
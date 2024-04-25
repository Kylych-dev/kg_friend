from rest_framework import serializers
from apps.quiz.models import (
    Category,
    Question,
    Answer,
    UserTestResult
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class UserTestResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserTestResult
        fields = '__all__'




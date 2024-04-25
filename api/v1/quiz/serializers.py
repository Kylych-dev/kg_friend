from rest_framework import serializers
from apps.quiz.models import (
    Category,
    Question,
    Answer,
    UserTestResult
)


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['question', 'answer']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category', 'questions']


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Question
        fields = [
            'question',
            'category',
            'answer'
        ]


class UserTestResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserTestResult
        fields = '__all__'




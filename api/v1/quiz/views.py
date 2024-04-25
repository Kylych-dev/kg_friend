from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from django.utils.translation import gettext as _

from .serializers import (
    CategorySerializer,
    AnswerSerializer,
    QuestionSerializer,
    UserTestResultSerializer
)

from apps.quiz.models import (
    Category,
    Question,
    Answer,
    UserTestResult
)

'''
Category
Question
Answer
UserTestResult
'''


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)


class StartQuizApiView(views.APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        submited_answers = request.data.get("answers", [])


        # category = None  # Переменная для хранения категории теста
        category = request.data.get("category")

        category = get_object_or_404(Category, pk=category)

        correct_answers = 0
        total_questions = len(submited_answers)

        for answer in submited_answers:
            question_id = answer.get("question")
            selected_answer_id = answer.get("selected_answer")
            # question = Question.objects.get(pk=question_id)
            question = get_object_or_404(Question, pk=question_id)
            correct_answer = question.answers.get(is_correct=True)
            if selected_answer_id == correct_answer.id:
                correct_answers += 1
        print(correct_answers, total_questions, '------------------------------------------')
        percentage = (correct_answers / total_questions) * 100 if total_questions > 0 else 0

        user_test_result = UserTestResult(
            user=request.user,
            category=category,
            correct_answers=correct_answers,
            # total_questions=total_questions,
            # percent_correct=percentage
        )
        user_test_result.save()

        serializer = UserTestResultSerializer(user_test_result)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


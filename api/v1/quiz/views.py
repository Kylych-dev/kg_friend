from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from django.utils.translation import gettext as _
from rest_framework.decorators import action

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from utils.customer_logger import log_error, log_warning

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

log_error(self, ex)
log_warning(self, ex)

'''


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)


class StartQuizApiView(views.APIView):

    @swagger_auto_schema(
        method="get",
        operation_description="Получить список вопросов.",
        operation_summary="Получить список вопросов",
        operation_id="list_questions",
        tags=["Quiz"],
        responses={200: openapi.Response(description="OK - Список вопросов получен успешно."),
                   401: openapi.Response(description="Ошибка аутентификации"),
                   404: openapi.Response(description="Not Found - Вопросы не найдены"),
                   },
    )
    @action(detail=False, methods=["get"])
    def get(self, request):
        try:
            questions = Question.objects.all()
            serializer = QuestionSerializer(questions, many=True)
            return Response(serializer.data)
        except Exception as ex:
            log_warning(self, ex)
            return Response(
                {"detail": "Internal Server Error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @swagger_auto_schema(
        method="post",
        operation_description="Отправить ответы пользователя.",
        operation_summary="Отправить ответы",
        operation_id="submit_answers",
        tags=["Quiz"],
        request_body=AnswerSerializer,
        responses={200: openapi.Response(description="OK - Ответы сохранены успешно."),
                   401: openapi.Response(description="Ошибка аутентификации"),
                   404: openapi.Response(description="Not Found - Вопросы или категория не найдены"),
                   },
    )
    @action(detail=False, methods=["post"])
    def post(self, request, *args, **kwargs):
        try:
            submited_answers = request.data.get("answers", [])
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

            percentage = (correct_answers / total_questions) * 100 if total_questions > 0 else 0

            user_test_result = UserTestResult(
                user=request.user,
                category=category,
                correct_answers=correct_answers,
                total_questions=total_questions,
                percent_correct=percentage
            )
            user_test_result.save()

            serializer = UserTestResultSerializer(user_test_result)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        except Exception as ex:
            log_warning(self, ex)
            return Response(
                {"detail": "Internal Server Error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

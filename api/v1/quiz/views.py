from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .serializers import (
    CategorySerializer,
    AnswerSerializer,
    QuestionSerializer,
    UserTestResultSerializer
)

from apps.quiz.models import (
    Question,
    Category,
    Answer,
    UserTestResult
)


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)








'''


from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Test, Question, UserTestResult
from .serializers import TestSerializer, QuestionSerializer, UserTestResultSerializer

class TestListView(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticated]

class TestStartView(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        test = self.get_object()
        # Начать тест для пользователя
        # Создать запись о начале теста для пользователя
        user_test_result = UserTestResult.objects.create(user=request.user, test=test)
        return Response({"message": "Test started successfully."})

class TestFinishView(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        test = self.get_object()
        # Завершить тест для пользователя
        # Подсчитать количество правильных ответов и обновить результат теста пользователя
        user_test_result = UserTestResult.objects.get(user=request.user, test=test)
        user_test_result.correct_answers = self.calculate_correct_answers(request.data)
        user_test_result.total_questions = test.questions.count()
        user_test_result.percentage = (user_test_result.correct_answers / user_test_result.total_questions) * 100
        user_test_result.save()
        return Response({"message": "Test finished successfully."})

    def calculate_correct_answers(self, data):
        # Рассчитать количество правильных ответов на основе данных, отправленных пользователем
        pass  # Реализуйте логику подсчета правильных ответов здесь


'''
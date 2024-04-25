from django.db import models
from ..account.models import CustomUser
import uuid


class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    category = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category


class Question(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='questions')
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default=5)

    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'questions'

    def __str__(self):
        return self.question


class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'answer'
        verbose_name_plural = 'answers'

    def __str__(self):
        return self.answer


class UserTestResult(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='test_result')
    test = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='user_result')
    correct_answers = models.PositiveIntegerField(default=0)
    total_questions = models.PositiveIntegerField(default=0)
    percent_correct = models.FloatField(default=0)

    class Meta:
        verbose_name = 'user test result'
        verbose_name_plural = 'user test results'

    def __str__(self):
        return self.user







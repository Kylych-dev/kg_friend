from django.contrib import admin
from .models import Category, Question, Answer, UserTestResult


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'created_at', 'updated_at']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'category', 'marks', 'created_at', 'updated_at']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer', 'question', 'is_correct', 'created_at', 'updated_at']


@admin.register(UserTestResult)
class UserTestResultAdmin(admin.ModelAdmin):
    list_display = ['user', 'test', 'correct_answers', 'total_questions', 'percent_correct']

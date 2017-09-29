from django.contrib import admin

from .models import Answer, Quiz, Question


class AnswerInline(admin.TabularInline):
    model = Answer
    fields = ['answer_title', 'is_correct', 'question']
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_title', 'quiz']
    inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz)

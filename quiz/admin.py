from django.contrib import admin

from .models import Choice, Quiz, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    fields = ['choice_title', 'is_correct', 'question']
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_title', 'quiz']
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz)

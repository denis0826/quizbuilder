from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session


class Quiz(models.Model):
    quiz_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    expiration = models.DateTimeField('expiration date')

    def __str__(self):
        return self.quiz_title

    class Meta:
        verbose_name_plural = 'quizzes'


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, null=True)
    question_title = models.CharField(max_length=600, blank=False)

    def __str__(self):
        return self.question_title


class Choice(models.Model):
    question = models.ForeignKey(Question)
    is_correct = models.BooleanField(default=False)
    choice_title = models.CharField(max_length=500)

    def __str__(self):
        return self.choice_title


class QuizSession(models.Model):
    # session = models.ForeignKey(Session)
    quiz = models.ForeignKey(Quiz)
    exam_date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.quiz.title


class Answer(models.Model):
    question = models.ForeignKey(Question)
    session = models.ForeignKey(QuizSession)
    chosen_answer = models.IntegerField()

    def __str__(self):
        return self.chosen_answer



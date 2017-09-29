from django.db import models
from django.contrib.auth.models import User


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


class Session(models.Model):
    quiz = models.ForeignKey(Quiz, null=True)
    exam_date = models.DateTimeField()
    score = models.IntegerField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.quiz.title


class Answer(models.Model):
    question = models.ForeignKey(Question, null=True)
    session = models.ForeignKey(Session, null=True)
    chosen_answer = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, null=True, blank=False)

    def __str__(self):
        return self.chosen_answer

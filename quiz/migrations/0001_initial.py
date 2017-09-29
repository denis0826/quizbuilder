# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exam_date', models.DateTimeField(auto_now_add=True, verbose_name=b'date taken')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_correct', models.BooleanField(default=False)),
                ('choice_title', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_title', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quiz_title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'date published')),
                ('expiration', models.DateTimeField(verbose_name=b'expiration date')),
            ],
            options={
                'verbose_name_plural': 'quizzes',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exam_date', models.DateTimeField()),
                ('score', models.IntegerField()),
                ('quiz', models.ForeignKey(to='quiz.Quiz', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(to='quiz.Quiz', null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='quiz.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='choice_answer',
            field=models.ForeignKey(to='quiz.Choice'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question_answer',
            field=models.ForeignKey(to='quiz.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='session_answer',
            field=models.ForeignKey(to='quiz.Session'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user_answer',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]

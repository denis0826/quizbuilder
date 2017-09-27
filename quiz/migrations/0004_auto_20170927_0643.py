# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0003_auto_20170926_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('exam_date', models.DateTimeField()),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(to='quiz.Quiz', null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', auto_now_add=True),
        ),
        migrations.AddField(
            model_name='session',
            name='quiz',
            field=models.ForeignKey(to='quiz.Quiz', null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]

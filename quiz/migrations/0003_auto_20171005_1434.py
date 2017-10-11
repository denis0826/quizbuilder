# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20171004_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='session',
            field=models.ForeignKey(to='quiz.QuizSession'),
        ),
        migrations.AlterField(
            model_name='quizsession',
            name='session',
            field=models.ForeignKey(to='sessions.Session'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_remove_quizsession_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='session',
            field=models.ForeignKey(to='quiz.QuizSession', null=True),
        ),
    ]

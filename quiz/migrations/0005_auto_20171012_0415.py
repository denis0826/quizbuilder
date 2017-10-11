# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20171012_0312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='session',
        ),
        migrations.AddField(
            model_name='quizsession',
            name='current_answer',
            field=models.ForeignKey(to='quiz.Answer', null=True),
        ),
    ]

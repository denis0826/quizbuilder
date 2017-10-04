# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='session',
            field=models.ForeignKey(to='sessions.Session'),
        ),
        migrations.AlterField(
            model_name='quizsession',
            name='session',
            field=models.ForeignKey(to='quiz.Answer'),
        ),
    ]

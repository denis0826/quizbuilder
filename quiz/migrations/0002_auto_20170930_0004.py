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
            name='question',
            field=models.ForeignKey(to='quiz.Question', null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='session',
            field=models.ForeignKey(to='quiz.Session', null=True),
        ),
    ]

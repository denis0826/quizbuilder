# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20171012_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizsession',
            name='exam_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='quizsession',
            name='quiz',
            field=models.ForeignKey(to='quiz.Quiz', null=True),
        ),
        migrations.AlterField(
            model_name='quizsession',
            name='score',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='quizsession',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]

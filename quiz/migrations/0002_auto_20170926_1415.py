# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name_plural': 'quizzes'},
        ),
        migrations.RenameField(
            model_name='question',
            old_name='text',
            new_name='question_title',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='title',
            new_name='quiz_title',
        ),
    ]

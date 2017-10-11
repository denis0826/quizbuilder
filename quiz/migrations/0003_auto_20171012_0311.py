# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20171012_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizsession',
            name='exam_date',
            field=models.DateTimeField(blank=True),
        ),
    ]

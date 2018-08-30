# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0013_auto_20180829_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson_history',
            name='lesson',
            field=models.ForeignKey(to='school.Lesson', verbose_name='ジャンル'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0012_auto_20180825_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson_history',
            name='lesson',
            field=models.ForeignKey(to='school.Lesson', verbose_name='ジャンル', related_name='lessonhistory'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_auto_20180825_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson_history',
            name='customer',
            field=models.ForeignKey(verbose_name='顧客名', to='school.Customer'),
        ),
        migrations.AlterField(
            model_name='lesson_history',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='受講日'),
        ),
        migrations.AlterField(
            model_name='lesson_history',
            name='hour',
            field=models.CharField(max_length=200, verbose_name='受講時間(h)'),
        ),
        migrations.AlterField(
            model_name='lesson_history',
            name='lesson',
            field=models.ForeignKey(verbose_name='ジャンル', to='school.Lesson'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_auto_20180823_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('hour', models.CharField(max_length=200, verbose_name='受講時間')),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='lesson_history',
            name='customer',
            field=models.ForeignKey(to='school.Customer'),
        ),
        migrations.AddField(
            model_name='lesson_history',
            name='lesson',
            field=models.ForeignKey(to='school.Lesson'),
        ),
    ]

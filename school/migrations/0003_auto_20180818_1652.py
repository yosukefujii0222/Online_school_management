# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='charge',
            field=models.CharField(max_length=200, verbose_name='基本料金'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='usage_fee',
            field=models.CharField(max_length=200, verbose_name='従量料金'),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.CharField(max_length=200, verbose_name='年齢'),
        ),
    ]

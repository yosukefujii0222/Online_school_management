# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('genre', models.IntegerField(choices=[(1, '英語'), (2, 'ファイナンス'), (3, 'プログラミング')], blank=True, verbose_name='ジャンル', null=True)),
                ('charge', models.IntegerField(verbose_name='基本料金')),
                ('usage_fee', models.IntegerField(verbose_name='従量料金')),
            ],
        ),
    ]

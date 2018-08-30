# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_auto_20180821_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lesson',
            field=models.ForeignKey(default=1, to='school.Lesson'),
            preserve_default=False,
        ),
    ]

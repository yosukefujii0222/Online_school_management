# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_auto_20180819_2337'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lesson_user',
            new_name='User',
        ),
    ]

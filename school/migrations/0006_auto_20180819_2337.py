# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Lesson_user',
        ),
    ]

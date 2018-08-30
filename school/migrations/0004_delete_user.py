# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20180818_1652'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]

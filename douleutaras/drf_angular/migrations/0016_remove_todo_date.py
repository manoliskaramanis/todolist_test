# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_angular', '0015_auto_20160626_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='date',
        ),
    ]

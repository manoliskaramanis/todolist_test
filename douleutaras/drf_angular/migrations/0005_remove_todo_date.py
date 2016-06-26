# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_angular', '0004_todo_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='date',
        ),
    ]

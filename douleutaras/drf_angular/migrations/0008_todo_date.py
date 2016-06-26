# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('drf_angular', '0007_remove_todo_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 6, 24, 20, 32, 1, 132410, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

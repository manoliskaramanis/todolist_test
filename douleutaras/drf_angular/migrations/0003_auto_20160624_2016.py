# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_angular', '0002_auto_20150527_1820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='is_completed',
            new_name='done',
        ),
    ]

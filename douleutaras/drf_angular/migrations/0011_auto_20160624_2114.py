# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_angular', '0010_todo_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=75)),
                ('password', models.CharField(max_length=75)),
            ],
        ),
        migrations.AlterField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(related_name='todos', to='drf_angular.User'),
        ),
    ]

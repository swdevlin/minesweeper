# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20160829_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='difficulty',
            field=models.IntegerField(default=1),
        ),
    ]
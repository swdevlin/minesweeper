# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 01:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20160829_2101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='diffculty',
            new_name='difficulty',
        ),
    ]

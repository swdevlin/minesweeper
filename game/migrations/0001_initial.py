# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 23:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.TextField()),
                ('flags', models.TextField()),
                ('playerBoard', models.TextField()),
                ('startedAt', models.DateTimeField(verbose_name='date started')),
            ],
        ),
    ]

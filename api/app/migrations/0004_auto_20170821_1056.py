# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-21 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_user_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar_url',
            field=models.TextField(blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('janitriapp', '0003_auto_20170523_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newswebsite',
            name='title',
            field=models.TextField(),
        ),
    ]
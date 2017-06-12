# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 19:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('janitriapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsWebsite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('description', models.TextField(blank=True)),
                ('news_website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='janitriapp.UserInterest')),
            ],
        ),
    ]
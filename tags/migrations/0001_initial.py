# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-24 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=120)),
                ('tiempo', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

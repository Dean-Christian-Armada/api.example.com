# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 10:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('sample_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='id',
        ),
        migrations.AddField(
            model_name='artist',
            name='getornonemodel_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.GetOrNoneModel'),
            preserve_default=False,
        ),
    ]

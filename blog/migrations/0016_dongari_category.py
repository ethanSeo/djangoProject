# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 11:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_remove_dongari_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='dongari',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.Category'),
        ),
    ]

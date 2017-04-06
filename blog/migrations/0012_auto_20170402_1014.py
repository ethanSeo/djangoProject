# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 10:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170402_0907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dongari',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='dongari',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.Dongari'),
        ),
    ]

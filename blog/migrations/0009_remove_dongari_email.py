# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 19:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170331_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dongari',
            name='email',
        ),
    ]

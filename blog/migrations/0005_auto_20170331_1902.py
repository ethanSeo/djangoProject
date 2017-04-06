# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170331_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='kr_name',
            field=models.CharField(help_text='분과명 (한국어)', max_length=20),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Club Category (English)', max_length=20),
        ),
    ]
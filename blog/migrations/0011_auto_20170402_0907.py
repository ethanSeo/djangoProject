# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_category_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='kr_name',
            new_name='kr_name_category',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='name_category',
        ),
        migrations.RenameField(
            model_name='dongari',
            old_name='kr_name',
            new_name='kr_name_dongari',
        ),
        migrations.RenameField(
            model_name='dongari',
            old_name='name',
            new_name='name_dongari',
        ),
        migrations.RemoveField(
            model_name='dongari',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='dongari',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Category'),
        ),
    ]

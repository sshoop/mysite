# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-04 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160904_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_title',
            field=models.CharField(max_length=50, verbose_name='标题'),
        ),
    ]

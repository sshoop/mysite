# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-08 05:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20160908_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_abstract',
            field=models.TextField(blank=True, help_text='可选 若为空则摘取前54个字符', null=True, verbose_name='摘要'),
        ),
    ]

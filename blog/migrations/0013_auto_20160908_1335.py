# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-08 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20160908_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_abstract',
            field=models.CharField(blank=True, help_text='可选 若为空则摘取前54个字符', max_length=256, null=True, verbose_name='摘要'),
        ),
    ]

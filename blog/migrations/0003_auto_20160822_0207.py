# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_article_abstract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], max_length=1, verbose_name='文章状态'),
        ),
    ]

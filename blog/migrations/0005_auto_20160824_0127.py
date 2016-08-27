# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 17:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160822_0252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_name', models.CharField(max_length=20, verbose_name='昵称')),
                ('comment_text', models.CharField(max_length=256, verbose_name='评论内容')),
                ('comment_create_time', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='article_top',
            field=models.BooleanField(default=False, verbose_name='草稿'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article', verbose_name='评论所属文章'),
        ),
    ]

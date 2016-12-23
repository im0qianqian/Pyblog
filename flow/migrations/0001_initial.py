# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-12-23 02:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_name', models.CharField(max_length=30)),
                ('meta_alias', models.CharField(blank=True, max_length=30)),
                ('meta_description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=30)),
                ('comment_author_email', models.EmailField(blank=True, max_length=254)),
                ('comment_author_url', models.URLField(blank=True)),
                ('comment_author_ip', models.GenericIPAddressField()),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('comment_content', models.TextField()),
                ('comment_parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flow.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_url', models.URLField(unique=True)),
                ('link_name', models.CharField(blank=True, max_length=30)),
                ('link_description', models.TextField(blank=True)),
                ('link_image', models.URLField(blank=True)),
                ('link_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flow.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('post_modified', models.DateTimeField(auto_now=True)),
                ('post_title', models.CharField(blank=True, max_length=40)),
                ('post_content', models.TextField(blank=True)),
                ('post_excerpt', models.TextField(blank=True)),
                ('post_status', models.BooleanField(default=False)),
                ('post_password', models.CharField(blank=True, max_length=30)),
                ('post_alias', models.CharField(blank=True, max_length=30)),
                ('post_image', models.URLField(blank=True)),
                ('post_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flow.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=30)),
                ('tag_alias', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='post_tag',
            field=models.ManyToManyField(blank=True, to='flow.Tag'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flow.Post'),
        ),
    ]

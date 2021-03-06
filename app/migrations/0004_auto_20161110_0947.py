# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 01:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_userprofile_online'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='department',
            field=models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='部门'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default=2, max_length=64, unique=True, verbose_name='邮箱'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='memo',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='备注'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='手机'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(default=2, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='tel',
            field=models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='座机'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='token',
            field=models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='token'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=32, verbose_name='名字'),
        ),
    ]

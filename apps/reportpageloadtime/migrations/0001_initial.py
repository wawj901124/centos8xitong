# Generated by Django 2.0.5 on 2020-04-23 09:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageLoadTimeReportFiveSecond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testproject', models.CharField(default='', max_length=100, verbose_name='测试项目')),
                ('testmodule', models.CharField(default='', max_length=100, verbose_name='测试模块')),
                ('testpage', models.CharField(default='', max_length=100, verbose_name='测试页面')),
                ('testcasetitle', models.CharField(default='', max_length=100, verbose_name='测试内容的名称')),
                ('teststarttime', models.CharField(default='', max_length=100, verbose_name='开始运行时间')),
                ('forcount', models.CharField(default='', max_length=100, verbose_name='第几次循环')),
                ('page_load_time_no_catch', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='页面加载时间（单位：毫秒）')),
                ('dom_load_time_no_catch', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='DOM加载时间（单位：毫秒）')),
                ('page_load_time_with_catch', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='有缓存时页面加载时间（单位：毫秒）')),
                ('dom_load_time_with_catch', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='有缓存时DOM加载时间（单位：毫秒）')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '页面加载时间在5秒及其以上统计',
                'verbose_name_plural': '页面加载时间在5秒及其以上统计',
            },
        ),
        migrations.CreateModel(
            name='PageLoadTimeReportFourSecond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testproject', models.CharField(default='', max_length=100, verbose_name='测试项目')),
                ('testmodule', models.CharField(default='', max_length=100, verbose_name='测试模块')),
                ('testpage', models.CharField(default='', max_length=100, verbose_name='测试页面')),
                ('testcasetitle', models.CharField(default='', max_length=100, verbose_name='测试内容的名称')),
                ('teststarttime', models.CharField(default='', max_length=100, verbose_name='开始运行时间')),
                ('forcount', models.CharField(default='', max_length=100, verbose_name='第几次循环')),
                ('page_load_time_no_catch', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='页面加载时间（单位：毫秒）')),
                ('dom_load_time_no_catch', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='DOM加载时间（单位：毫秒）')),
                ('page_load_time_with_catch', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='有缓存时页面加载时间（单位：毫秒）')),
                ('dom_load_time_with_catch', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='有缓存时DOM加载时间（单位：毫秒）')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '页面加载时间在4秒至5秒统计',
                'verbose_name_plural': '页面加载时间在4秒至5秒统计',
            },
        ),
        migrations.CreateModel(
            name='PageLoadTimeReportOneSecond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testproject', models.CharField(default='', max_length=100, verbose_name='测试项目')),
                ('testmodule', models.CharField(default='', max_length=100, verbose_name='测试模块')),
                ('testpage', models.CharField(default='', max_length=100, verbose_name='测试页面')),
                ('testcasetitle', models.CharField(default='', max_length=100, verbose_name='测试内容的名称')),
                ('teststarttime', models.CharField(default='', max_length=100, verbose_name='开始运行时间')),
                ('forcount', models.CharField(default='', max_length=100, verbose_name='第几次循环')),
                ('page_load_time_no_catch', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='页面加载时间（单位：毫秒）')),
                ('dom_load_time_no_catch', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='DOM加载时间（单位：毫秒）')),
                ('page_load_time_with_catch', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='有缓存时页面加载时间（单位：毫秒）')),
                ('dom_load_time_with_catch', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='有缓存时DOM加载时间（单位：毫秒）')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '页面加载时间在1秒至2秒统计',
                'verbose_name_plural': '页面加载时间在1秒至2秒统计',
            },
        ),
        migrations.CreateModel(
            name='PageLoadTimeReportThereSecond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testproject', models.CharField(default='', max_length=100, verbose_name='测试项目')),
                ('testmodule', models.CharField(default='', max_length=100, verbose_name='测试模块')),
                ('testpage', models.CharField(default='', max_length=100, verbose_name='测试页面')),
                ('testcasetitle', models.CharField(default='', max_length=100, verbose_name='测试内容的名称')),
                ('teststarttime', models.CharField(default='', max_length=100, verbose_name='开始运行时间')),
                ('forcount', models.CharField(default='', max_length=100, verbose_name='第几次循环')),
                ('page_load_time_no_catch', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='页面加载时间（单位：毫秒）')),
                ('dom_load_time_no_catch', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='DOM加载时间（单位：毫秒）')),
                ('page_load_time_with_catch', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='有缓存时页面加载时间（单位：毫秒）')),
                ('dom_load_time_with_catch', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='有缓存时DOM加载时间（单位：毫秒）')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '页面加载时间在3秒至4秒统计',
                'verbose_name_plural': '页面加载时间在3秒至4秒统计',
            },
        ),
        migrations.CreateModel(
            name='PageLoadTimeReportTwoSecond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testproject', models.CharField(default='', max_length=100, verbose_name='测试项目')),
                ('testmodule', models.CharField(default='', max_length=100, verbose_name='测试模块')),
                ('testpage', models.CharField(default='', max_length=100, verbose_name='测试页面')),
                ('testcasetitle', models.CharField(default='', max_length=100, verbose_name='测试内容的名称')),
                ('teststarttime', models.CharField(default='', max_length=100, verbose_name='开始运行时间')),
                ('forcount', models.CharField(default='', max_length=100, verbose_name='第几次循环')),
                ('page_load_time_no_catch', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='页面加载时间（单位：毫秒）')),
                ('dom_load_time_no_catch', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='DOM加载时间（单位：毫秒）')),
                ('page_load_time_with_catch', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='有缓存时页面加载时间（单位：毫秒）')),
                ('dom_load_time_with_catch', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='有缓存时DOM加载时间（单位：毫秒）')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '页面加载时间在2秒至3秒统计',
                'verbose_name_plural': '页面加载时间在2秒至3秒统计',
            },
        ),
    ]

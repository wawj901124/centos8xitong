# Generated by Django 2.0.5 on 2020-07-04 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiderdata', '0006_spiderweburl'),
    ]

    operations = [
        migrations.AddField(
            model_name='spiderweburl',
            name='modify_url_title',
            field=models.CharField(blank=True, default='', max_length=1500, null=True, verbose_name='修改后网站标题'),
        ),
        migrations.AddField(
            model_name='spiderweburl',
            name='modify_web_url',
            field=models.CharField(blank=True, default='', max_length=1500, null=True, verbose_name='修改后web网址'),
        ),
    ]
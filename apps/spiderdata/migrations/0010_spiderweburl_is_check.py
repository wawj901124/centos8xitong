# Generated by Django 2.0.5 on 2020-07-04 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiderdata', '0009_auto_20200704_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='spiderweburl',
            name='is_check',
            field=models.BooleanField(default=False, verbose_name='是否已看'),
        ),
    ]

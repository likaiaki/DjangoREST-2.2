# Generated by Django 2.1.8 on 2020-03-21 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200321_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='gender',
            field=models.SmallIntegerField(choices=[(0, '男'), (1, '女')], default=0, verbose_name='性别'),
        ),
    ]

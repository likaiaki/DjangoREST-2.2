# Generated by Django 2.1.8 on 2020-03-26 02:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_remove_blog_allow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, to_field='mobile', verbose_name='用户id'),
        ),
    ]

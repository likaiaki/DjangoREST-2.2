# Generated by Django 2.1.8 on 2020-03-21 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='blog_id',
            new_name='blog',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='parent_id',
            new_name='parent',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user',
        ),
    ]
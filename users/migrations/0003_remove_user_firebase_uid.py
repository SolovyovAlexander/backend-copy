# Generated by Django 3.1 on 2020-09-14 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_firebase_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='firebase_uid',
        ),
    ]
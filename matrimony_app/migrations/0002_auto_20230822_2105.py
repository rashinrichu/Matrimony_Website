# Generated by Django 3.2.16 on 2023-08-22 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='nativity',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
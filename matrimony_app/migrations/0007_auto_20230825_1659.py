# Generated by Django 3.2.16 on 2023-08-25 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony_app', '0006_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriptionplan',
            name='duration_months',
        ),
        migrations.RemoveField(
            model_name='subscriptionplan',
            name='price',
        ),
    ]
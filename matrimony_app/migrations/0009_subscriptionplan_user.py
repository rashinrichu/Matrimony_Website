# Generated by Django 3.2.16 on 2023-08-28 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony_app', '0008_auto_20230825_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionplan',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='matrimony_app.userprofile'),
        ),
    ]

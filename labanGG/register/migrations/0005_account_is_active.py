# Generated by Django 4.2.10 on 2024-03-16 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_account_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
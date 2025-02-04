# Generated by Django 4.1.2 on 2022-11-18 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0008_alter_users_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(blank=True, db_index=True, error_messages={'unique': 'A user with such username already exists, please, try another one'}, max_length=255, unique=True),
        ),
    ]

# Generated by Django 4.1.2 on 2022-11-21 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0012_alter_subjects_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiletypes',
            name='profile_type',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]

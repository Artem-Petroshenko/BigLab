# Generated by Django 4.1.2 on 2022-11-21 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0013_alter_profiletypes_profile_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentteacher',
            name='subject',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.0.8 on 2020-07-14 13:19

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('profile_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]

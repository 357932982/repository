# Generated by Django 2.0.2 on 2018-03-07 14:13

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userinfo',
            managers=[
                ('user', django.db.models.manager.Manager()),
            ],
        ),
    ]

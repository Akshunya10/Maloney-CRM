# Generated by Django 3.2.23 on 2024-01-14 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_users_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'managed': True},
        ),
    ]

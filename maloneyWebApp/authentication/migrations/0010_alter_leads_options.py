# Generated by Django 3.2.23 on 2024-01-26 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_alter_leads_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leads',
            options={'managed': False},
        ),
    ]
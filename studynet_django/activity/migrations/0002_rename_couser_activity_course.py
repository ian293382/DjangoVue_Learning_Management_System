# Generated by Django 5.0 on 2024-01-14 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='couser',
            new_name='course',
        ),
    ]
# Generated by Django 5.0 on 2024-01-15 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_course_created_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('in_review', 'In_review'), ('published', 'Published')], default='draft', max_length=25),
        ),
    ]

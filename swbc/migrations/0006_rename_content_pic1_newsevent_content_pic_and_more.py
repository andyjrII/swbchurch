# Generated by Django 5.0.1 on 2024-01-28 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swbc', '0005_rename_service_details_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsevent',
            old_name='content_pic1',
            new_name='content_pic',
        ),
        migrations.RemoveField(
            model_name='newsevent',
            name='content_pic2',
        ),
        migrations.RemoveField(
            model_name='service',
            name='content_pic',
        ),
    ]

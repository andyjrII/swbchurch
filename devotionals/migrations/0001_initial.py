# Generated by Django 4.2.9 on 2024-02-23 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devotional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('contents', models.TextField(blank=True)),
                ('date', models.DateField(null=True)),
                ('reference_text', models.TextField(blank=True)),
                ('daily_bible_reading', models.CharField(max_length=255)),
                ('week_teaching', models.CharField(max_length=255)),
                ('confession', models.TextField(blank=True)),
            ],
        ),
    ]

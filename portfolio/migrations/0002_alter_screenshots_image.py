# Generated by Django 5.1.4 on 2025-01-11 12:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="screenshots",
            name="image",
            field=models.ImageField(upload_to="project_screenshots"),
        ),
    ]

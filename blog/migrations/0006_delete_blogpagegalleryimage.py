# Generated by Django 5.0.4 on 2024-05-08 04:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0005_alter_blogpagegalleryimage_image"),
    ]

    operations = [
        migrations.DeleteModel(
            name="BlogPageGalleryImage",
        ),
    ]

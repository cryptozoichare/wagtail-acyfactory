# Generated by Django 5.0.4 on 2024-05-08 04:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0007_customimage_caption"),
        ("blog", "0004_alter_blogcategory_icon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpagegalleryimage",
            name="image",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="base.customimage",
            ),
        ),
    ]

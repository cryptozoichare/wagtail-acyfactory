# Generated by Django 5.0.4 on 2024-05-28 02:42

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0009_remove_normalpage_image_alter_normalpage_body"),
        ("blog", "0017_blogpage_caption"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpage",
            name="alt",
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name="blogpage",
            name="caption",
            field=wagtail.fields.RichTextField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name="blogpage",
            name="image",
            field=models.ForeignKey(
                blank=True,
                help_text="Landscape suggested.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="base.customimage",
            ),
        ),
    ]

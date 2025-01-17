# Generated by Django 5.0.4 on 2024-05-28 07:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0010_remove_formpage_page_ptr_delete_formfield_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DesignSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "banner",
                    models.ForeignKey(
                        blank=True,
                        help_text="Landscape suggested.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="base.customimage",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]

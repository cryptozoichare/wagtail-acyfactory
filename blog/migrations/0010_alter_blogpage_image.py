# Generated by Django 5.0.4 on 2024-05-13 08:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0008_alter_footertext_unique_together_and_more"),
        ("blog", "0009_blogpage_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpage",
            name="image",
            field=models.ForeignKey(
                blank=True,
                help_text="Landscape mode only; horizontal width between 1000px and 3000px.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="base.customimage",
            ),
        ),
    ]

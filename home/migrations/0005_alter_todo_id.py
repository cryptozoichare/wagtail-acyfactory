# Generated by Django 5.0.4 on 2024-05-23 22:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_todo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-23 22:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0014_rename_commentwithtitle_blogcomment"),
    ]

    operations = [
        migrations.DeleteModel(
            name="BlogComment",
        ),
    ]
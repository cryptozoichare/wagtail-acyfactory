# Generated by Django 5.0.4 on 2024-05-09 22:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0007_customimage_caption"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="footertext",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="footertext",
            name="latest_revision",
        ),
        migrations.RemoveField(
            model_name="footertext",
            name="live_revision",
        ),
        migrations.RemoveField(
            model_name="footertext",
            name="locale",
        ),
        migrations.DeleteModel(
            name="NavigationSettings",
        ),
        migrations.DeleteModel(
            name="FooterText",
        ),
    ]

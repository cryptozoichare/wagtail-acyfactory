# Generated by Django 5.0.4 on 2024-05-09 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blogpage_body_alter_blogpage_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='date',
        ),
    ]
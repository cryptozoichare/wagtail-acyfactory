# Generated by Django 5.0.4 on 2024-05-28 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestbookentry',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]

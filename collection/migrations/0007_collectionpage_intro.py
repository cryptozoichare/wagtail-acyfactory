# Generated by Django 5.0.4 on 2024-06-09 21:46

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0006_rename_desginer_product_designer'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectionpage',
            name='intro',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]

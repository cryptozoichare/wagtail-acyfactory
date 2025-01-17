# Generated by Django 5.1.4 on 2024-12-31 21:35

import base.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_customimage_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normalpage',
            name='body',
            field=wagtail.fields.StreamField([('heading_block', 2), ('paragraph_block', 3), ('image_block', 6), ('embed_block', 7), ('html_block', 8), ('link_button_block', 9)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'form_classname': 'title', 'required': True}), 1: ('wagtail.blocks.ChoiceBlock', [], {'blank': True, 'choices': [('', 'Select a heading size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], 'required': False}), 2: ('wagtail.blocks.StructBlock', [[('heading_text', 0), ('size', 1)]], {}), 3: ('wagtail.blocks.RichTextBlock', (), {'icon': 'pilcrow'}), 4: ('wagtail.images.blocks.ImageBlock', [], {}), 5: ('wagtail.blocks.CharBlock', (), {'required': False}), 6: ('wagtail.blocks.StructBlock', [[('image', 4), ('caption', 5), ('attribution', 5)]], {}), 7: ('wagtail.embeds.blocks.EmbedBlock', (), {'help_text': 'Insert a URL to embed. For example, https://www.youtube.com/watch?v=SGJFWirQ3ks', 'icon': 'media'}), 8: ('wagtail.blocks.RawHTMLBlock', (), {}), 9: ('wagtail.blocks.ListBlock', (base.blocks.LinkButtonBlock,), {'template': 'base/blocks/link_button_list.html'})}, verbose_name='Page body'),
        ),
    ]

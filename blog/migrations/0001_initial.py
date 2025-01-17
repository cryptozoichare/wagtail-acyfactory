# Generated by Django 5.0.4 on 2024-05-08 03:10

import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.blocks
import wagtail.contrib.routable_page.models
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        (
            "taggit",
            "0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx",
        ),
        ("wagtailcore", "0093_uploadedfile"),
        ("wagtailimages", "0026_delete_uploadedimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "introduction",
                    models.TextField(blank=True, help_text="Text to describe the page"),
                ),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        help_text="Landscape mode only; horizontal width between 1000px and 3000px.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(
                wagtail.contrib.routable_page.models.RoutablePageMixin,
                "wagtailcore.page",
            ),
        ),
        migrations.CreateModel(
            name="BlogPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "introduction",
                    models.TextField(blank=True, help_text="Text to describe the page"),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            (
                                "heading_block",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "heading_text",
                                            wagtail.blocks.CharBlock(
                                                form_classname="title", required=True
                                            ),
                                        ),
                                        (
                                            "size",
                                            wagtail.blocks.ChoiceBlock(
                                                blank=True,
                                                choices=[
                                                    ("", "Select a heading size"),
                                                    ("h2", "H2"),
                                                    ("h3", "H3"),
                                                    ("h4", "H4"),
                                                ],
                                                required=False,
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "paragraph_block",
                                wagtail.blocks.RichTextBlock(icon="pilcrow"),
                            ),
                            (
                                "image_block",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(
                                                required=True
                                            ),
                                        ),
                                        (
                                            "caption",
                                            wagtail.blocks.CharBlock(required=False),
                                        ),
                                        (
                                            "attribution",
                                            wagtail.blocks.CharBlock(required=False),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "embed_block",
                                wagtail.embeds.blocks.EmbedBlock(
                                    help_text="Insert a URL to embed. For example, https://www.youtube.com/watch?v=SGJFWirQ3ks",
                                    icon="media",
                                ),
                            ),
                        ],
                        blank=True,
                        verbose_name="Page body",
                    ),
                ),
                ("subtitle", models.CharField(blank=True, max_length=255)),
                (
                    "date_published",
                    models.DateField(
                        blank=True, null=True, verbose_name="Date article published"
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        help_text="Landscape mode only; horizontal width between 1000px and 3000px.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="BlogPageTag",
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
                    "content_object",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tagged_items",
                        to="blog.blogpage",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s_items",
                        to="taggit.tag",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="blogpage",
            name="tags",
            field=modelcluster.contrib.taggit.ClusterTaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="blog.BlogPageTag",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]

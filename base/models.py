from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page
from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
)
from wagtail.fields import RichTextField, StreamField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel

from wagtail.images.models import Image, AbstractImage, AbstractRendition
from wagtail.documents.models import Document, AbstractDocument
from base.blocks import BaseStreamBlock


class FormField(AbstractFormField):
    page = ParentalKey("FormPage", on_delete=models.CASCADE, related_name="form_fields")


class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel("intro"),
        InlinePanel("form_fields", label="Form fields"),
        FieldPanel("thank_you_text"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("from_address"),
                        FieldPanel("to_address"),
                    ]
                ),
                FieldPanel("subject"),
            ],
            "Email",
        ),
    ]


class NormalPage(Page):
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True, use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


class CustomImage(AbstractImage):
    # Add any extra fields to image here

    # To add a caption field:
    caption = models.CharField(max_length=255, blank=True)

    admin_form_fields = Image.admin_form_fields + (
        # Then add the field names here to make them appear in the form:
        "caption",
    )


class CustomRendition(AbstractRendition):
    image = models.ForeignKey(
        CustomImage, on_delete=models.CASCADE, related_name="renditions"
    )

    class Meta:
        unique_together = (("image", "filter_spec", "focal_point_key"),)


class CustomDocument(AbstractDocument):
    # Custom field example:
    source = models.CharField(max_length=255, blank=True, null=True)

    admin_form_fields = Document.admin_form_fields + (
        # Add all custom fields names to make them appear in the form:
        "source",
    )

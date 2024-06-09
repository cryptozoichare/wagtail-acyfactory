from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import (
    FieldPanel,
)
from wagtail.fields import StreamField, RichTextField
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)

from wagtail.images.models import Image, AbstractImage, AbstractRendition
from wagtail.documents.models import Document, AbstractDocument
from base.blocks import BaseStreamBlock


class NormalPage(Page):
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True, use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
    
class GenericIndexPage(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("intro", classname="full"),
    ]
    def get_descendants(self):
        return self.get_children().live()


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


@register_setting
class DesignSettings(BaseGenericSetting):
    banner = models.ForeignKey(
        "base.CustomImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Landscape suggested.",
    )
    logo = models.ForeignKey(
        "base.CustomImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Square suggested.",
    )

    panels = [
        FieldPanel("banner"),
        FieldPanel("logo"),
    ]

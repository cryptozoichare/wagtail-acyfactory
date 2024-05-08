from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from base.blocks import BaseStreamBlock

class HomePage(Page):
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True, use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
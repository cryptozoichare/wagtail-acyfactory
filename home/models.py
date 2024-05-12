from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from base.blocks import BaseStreamBlock
from blog.models import BlogPage, BlogIndexPage


class HomePage(Page):
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True, use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
    

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = BlogPage.objects.live().descendant_of(self).order_by('-first_published_at')
        context['blogpages'] = blogpages[0:6]
        return context
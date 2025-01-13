from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel
from django.utils.translation import gettext_lazy as _
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
class DoodlePage(Page):
    intro = RichTextField(blank=True)
    max_width = models.IntegerField(
        default=800,
        help_text="Canvas width in pixels"
    )
    max_height = models.IntegerField(
        default=600,
        help_text="Canvas height in pixels"
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('max_width'),
        FieldPanel('max_height'),
    ]
    
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
    ]
    
    template = 'doodle/doodle_page.html'
    
    class Meta:
        verbose_name = 'Doodle Page'


@register_snippet
class Doodle(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    # Store doodle data as JSON to keep stroke info, colors, etc.
    doodle_data = models.JSONField()
    # If you want to store as image instead/additionally
    image = models.ImageField(upload_to='doodle/', null=True, blank=True)
    
    panels = [
        FieldPanel('title'),
        FieldPanel('doodle_data'),
        FieldPanel('image'),
    ]
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Doodle')
        verbose_name_plural = _('Doodles')
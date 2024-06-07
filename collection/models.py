from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet

# Create your models here.

@register_snippet
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('vpet', 'Virtual pet'),
        ('pin', 'Enamel Pin'),
    ]
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ForeignKey(
        "base.CustomImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    def __str__(self):
        return self.name
    
class CollectionPage(Page):
    category = models.CharField(
        max_length=20,
        choices=Product.CATEGORY_CHOICES,
    )

    content_panels = Page.content_panels + [
        FieldPanel('category'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['products'] = Product.objects.filter(category=self.category)
        return context
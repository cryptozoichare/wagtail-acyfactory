from django.db import models
from django.shortcuts import render
from django.utils import timezone
from django_comments.abstracts import CommentAbstractModel
from wagtail.models import Page
from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
)
from wagtail.fields import RichTextField, StreamField
from wagtail.snippets.models import register_snippet
from base.blocks import BaseStreamBlock

class GuestbookPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]
    def serve(self, request):
        from guestbook.forms import GuestbookForm

        if request.method == 'POST':
            form = GuestbookForm(request.POST)
            if form.is_valid():
                form.save()      
                return render(request, 'guestbook/thankyou.html', {
                    'page': self,
                })
        else:
            form = GuestbookForm()

        return render(request, 'guestbook/guestbook_page.html', {
            'page': self,
            'form': form,
        })

@register_snippet
class GuestbookComment(models.Model):
    page = models.ForeignKey('guestbook.GuestbookPage', on_delete=models.CASCADE, related_name='comments')
    user_name = models.CharField(max_length=50, blank=True)
    user_url = models.URLField(blank=True)
    comment = models.TextField(max_length=3000)
    submit_date = models.DateTimeField(default=timezone.now, db_index=True)
    panels = [
        FieldPanel("user_name"),
        FieldPanel("user_url"),
        FieldPanel("comment"),
        FieldPanel("submit_date"),
    ]
    def __str__(self):
        return self.comment
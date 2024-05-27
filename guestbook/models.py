from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.snippets.models import register_snippet
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from honeypot.decorators import check_honeypot

class GuestbookEntry(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.message[:20]}"

@method_decorator(check_honeypot, name='serve')
class GuestbookPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['entries'] = GuestbookEntry.objects.order_by('-submitted_at')
        return context

    def serve(self, request):
        from .forms import GuestbookForm  # Move the import inside the method to avoid circular import

        form = GuestbookForm()

        if request.method == 'POST':
            form = GuestbookForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(self.url)

        context = self.get_context(request)
        context['form'] = form
        return render(request, 'guestbook/guestbook_page.html', context)

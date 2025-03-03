from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page

from base.blocks import BaseStreamBlock
from blog.models import BlogPage


class HomePage(Page):
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True, use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        InlinePanel("updates"),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        context['latest_updates'] = self.updates.order_by('-id')[:3]
        blogpages = (
            BlogPage.objects.live().descendant_of(self).order_by("-first_published_at")
        )
        context["blogpages"] = blogpages[:3]
        return context


# class Todo(models.Model):
#     text = models.CharField(max_length=255)
#     status = models.BooleanField(default=False)

#     def __str__(self):
#         return self.text

class Update(models.Model):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='updates')
    update = RichTextField()
    date = models.DateField(auto_now_add=True)

    panels = [
        FieldPanel("update"),
    ]

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


class UpdatesPage(Page):
    intro = RichTextField(blank=True)
    updates_per_page = 10  # You can adjust this number

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        
        # Get all updates from the homepage
        homepage = self.get_parent()
        updates = homepage.updates.order_by('-id')

        # Pagination
        paginator = Paginator(updates, self.updates_per_page)
        page = request.GET.get('page')
        
        try:
            updates_page = paginator.page(page)
        except PageNotAnInteger:
            updates_page = paginator.page(1)
        except EmptyPage:
            updates_page = paginator.page(paginator.num_pages)

        context['updates_page'] = updates_page
        return context
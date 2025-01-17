from django.contrib.syndication.views import Feed
from .models import BlogPage


class BlogFeed(Feed):
    title = "Acy Factory"
    link = "/blog/"
    description = "The blog of Acy Factory."

    def items(self):
        return BlogPage.objects.live().order_by("-first_published_at")[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.intro

    def item_link(self, item):
        return item.get_absolute_url()
from django.contrib.syndication.views import Feed

from .models import BlogPage


class BlogFeed(Feed):
    title = "Acy Factory"
    link = "/blog/"
    author_name = "Acy Factory"
    item_author_name = "Acy Factory"
    author_link = "https://acyfactory.com/"
    item_author_link = "https://acyfactory.com/"
    feed_url = "/blog/feed/"

    def items(self):
        return BlogPage.objects.live().public().order_by("-first_published_at")[:20]

    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return item.full_url

    def item_pubdate(self, item):
        """
        Takes an item, as returned by items(), and returns the item's
        pubdate.
        """
        return item.first_published_at

    def item_description(self, item):
        page = item.specific
        html = str(page.body)
        return html
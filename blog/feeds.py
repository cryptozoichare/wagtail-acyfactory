# blog/feeds.py
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed, Atom1Feed
from django.utils.html import strip_tags
from django.utils.timezone import make_aware
from wagtail.models import Site
from wagtail.rich_text import expand_db_html
from .models import BlogPage

# --- RSS generator that adds <content:encoded> like WordPress ---
class WPStyleRSSFeed(Rss201rev2Feed):
    content_type = 'application/rss+xml; charset=utf-8'

    def root_attributes(self):
        attrs = super().root_attributes()
        # WordPress-like full-content namespace
        attrs["xmlns:content"] = "http://purl.org/rss/1.0/modules/content/"
        return attrs

    def add_item_elements(self, handler, item):
        super().add_item_elements(handler, item)
        full = item.get("content_encoded")
        if full:
            # IMPORTANT: this tag is wrapped in CDATA by feedgenerator automatically
            handler.addQuickElement("content:encoded", full)


class LatestPostsBase(Feed):
    # populated in get_object so we can build absolute URLs
    site = None
    request = None

    title = "My Wagtail Blog"
    link = "/blog/"
    description = "Latest blog posts"

    def get_object(self, request, *args, **kwargs):
        self.request = request
        self.site = Site.find_for_request(request)
        return None

    def items(self):
        return (
            BlogPage.objects.live()
            .order_by("-first_published_at")
            .select_related()[:20]
        )

    # ----- Per-item fields -----
    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body.stream_block.render(item.body) or item.intro

    def item_link(self, item):
        # Absolute URL for the current Site
        if self.site:
            return f"{self.site.root_url}{item.url}"
        # Fallbacks if Site not resolved (rare)
        return getattr(item, "full_url", None) or item.url

    def item_pubdate(self, item):
        # Use .date (a DateField) as naive date -> make aware at midnight
        from datetime import datetime, time
        dt = datetime.combine(item.first_published_at, time.min)
        return make_aware(dt)

    def item_categories(self, item):
        # Use tag names like WordPress <category>
        return [t.name for t in getattr(item, "tags").all()]

    def item_extra_kwargs(self, item):
        html = item.body.stream_block.render(item.body)
        return {"content_encoded": html, "content": html}


# --- RSS feed with <content:encoded> ---
class LatestPostsRSSFeed(LatestPostsBase):
    feed_type = WPStyleRSSFeed


# --- Atom feed with <content> ---
class LatestPostsAtomFeed(LatestPostsBase):
    feed_type = Atom1Feed
    subtitle = LatestPostsBase.description

    # Atom generator uses "content" from item_extra_kwargs
    # Nothing else to override.

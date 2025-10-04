# blog/urls.py
from django.urls import path
from .feeds import LatestPostsRSSFeed, LatestPostsAtomFeed

urlpatterns = [
    path("feed/rss/", LatestPostsRSSFeed(), name="blog_feed_rss"),
    path("feed/atom/", LatestPostsAtomFeed(), name="blog_feed_atom"),
]

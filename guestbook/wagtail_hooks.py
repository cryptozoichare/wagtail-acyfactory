from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from .models import GuestbookEntry


class GustbookViewSet(SnippetViewSet):
    model = GuestbookEntry
    copy_view_enabled = False
    inspect_view_enabled = True


register_snippet(GustbookViewSet)

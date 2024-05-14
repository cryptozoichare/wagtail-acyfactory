from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel

from home.models import Todo

class TodoViewSet(SnippetViewSet):
    model = Todo

    panels = [
        FieldPanel("text"),
        FieldPanel("status"),
    ]

register_snippet(Todo)
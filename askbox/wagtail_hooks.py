# wagtail_hooks.py
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel

from .models import Question

class QuestionViewSet(SnippetViewSet):
    model = Question
    panels = [
        FieldPanel('question_text'),
        FieldPanel('answer_text'),
        FieldPanel('is_answered'),
    ]

register_snippet(QuestionViewSet)

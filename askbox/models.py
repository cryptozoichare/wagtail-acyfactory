# models.py
from django.db import models
from wagtail.admin.panels import FieldPanel

class Question(models.Model):
    question_text = models.TextField("Question")
    answer_text = models.TextField("Answer", blank=True)
    is_answered = models.BooleanField(default=False)
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.question_text[:50]}{'...' if len(self.question_text) > 50 else ''}"

    panels = [
        FieldPanel('question_text'),
        FieldPanel('answer_text'),
        FieldPanel('is_answered'),
    ]

from wagtail.models import Page
from django.shortcuts import render
from .forms import QuestionForm
from django.utils.decorators import method_decorator
from honeypot.decorators import check_honeypot

@method_decorator(check_honeypot, name="serve")
class AskQuestionPage(Page):

    def get_context(self, request):
        context = super().get_context(request)
        context['form'] = QuestionForm()
        context['answered_questions'] = Question.objects.filter(is_answered=True)
        return context

    def serve(self, request):
        if request.method == 'POST':
            form = QuestionForm(request.POST)
            if form.is_valid():
                form.save()
                form = QuestionForm()  # Reset the form after submission
        else:
            form = QuestionForm()

        context = self.get_context(request)
        context['form'] = form
        return render(request, "askbox/ask_question_page.html", context)

    content_panels = Page.content_panels + [
        FieldPanel('title'),
    ]
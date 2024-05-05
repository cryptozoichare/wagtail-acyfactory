from django.db import models
from django.views.generic.detail import DetailView

# import parentalKey:
from modelcluster.fields import ParentalKey, ParentalManyToManyField

# import FieldRowPanel and InlinePanel:
from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PublishingPanel,
)

from wagtail.fields import RichTextField
from wagtail.models import (
    Page,
    DraftStateMixin,
    PreviewableMixin,
    RevisionMixin,
    TranslatableMixin,
)

# import AbstractEmailForm and AbstractFormField:
from wagtail.contrib.forms.models import AbstractForm, AbstractFormField, AbstractFormSubmission

from wagtail.search import index

# import FormSubmissionsPanel:
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)
from wagtail.snippets.models import register_snippet


# ... keep the definition of NavigationSettings and FooterText. Add FormField and FormPage:
class FormField(AbstractFormField):
    page = ParentalKey('GuestbookPage', on_delete=models.CASCADE, related_name='form_fields')


class GuestbookPage(AbstractForm, Page):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text'),
    ]
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # Retrieve all form submissions for the current page
        submissions = self.get_submission_class().objects.filter(page=self)

        # Extract raw form data from submissions
        raw_data = []
        for submission in submissions:
            raw_data.append(submission.get_data())

        # Add raw form data to the context
        context.update({
            'raw_data': raw_data,
        })
        return context
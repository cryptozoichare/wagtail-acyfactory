from django.forms import ModelForm
from .models import GuestbookComment

class GuestbookForm(ModelForm):
    class Meta:
        model = GuestbookComment
        fields = ["user_name", "user_url", "comment"]
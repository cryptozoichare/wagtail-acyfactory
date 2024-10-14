# forms.py
from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        widgets = {
            'question_text': forms.Textarea(attrs={'placeholder': 'Ask your question here...'}),
        }
        labels = {
            'question_text': 'Your Question',
        }

from django import forms
from .models import Event, EmailTemplate

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_type', 'date']

class EmailTemplateForm(forms.ModelForm):
    class Meta:
        model = EmailTemplate
        fields = ['event_type', 'template']

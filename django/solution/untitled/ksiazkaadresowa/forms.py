import re

from django.core.exceptions import ValidationError
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Person


class ContactUsForm(forms.Form):
    sender = forms.EmailField()
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)


class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name']

    def regex(self, pattern, text):
        if not re.match(pattern, text):
            raise ValidationError(_(f'Invalid character'))

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        first_name = first_name.title()

        self.regex(
            pattern=r'^\w\w[\s\w-]*\w$',
            text=first_name,
        )

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        last_name = last_name.title()

        self.regex(
            pattern=r'^\w\w[\s\w-]*\w$',
            text=last_name,
        )

        return last_name

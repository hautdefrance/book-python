from django import forms
from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name']

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']

        if 'x' in first_name:
            raise forms.ValidationError("X in first_name")
        else:
            return first_name

from django import forms
from django.views.generic import FormView, TemplateView


class ContactUsForm(forms.Form):
    sender = forms.EmailField()
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)


class ContactUsView(FormView):
    template_name = 'ksiazkaadresowa/contact-form.html'
    form_class = ContactUsForm
    success_url = '/thank-you.html'


class ThankYouView(TemplateView):
    template_name = 'ksiazkaadresowa/thank-you.html'

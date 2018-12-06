from django.views.generic import TemplateView
from .models import Person


class ContactView(TemplateView):
    template_name = 'ksiazkaadresowa/templates/ksiazkaadresowa/contact.html'

    def get_context_data(self, **kwargs):
        return {
            'contacts': Person.objects.all()
        }

from http import HTTPStatus
from django.http import JsonResponse
from django.views.generic import TemplateView, View
from .models import Person


class ContactHTML(TemplateView):
    template_name = 'ksiazkaadresowa/contact.html'

    def get_context_data(self, **kwargs):
        return {
            'contacts': Person.objects.all()
        }


class ContactCSV(TemplateView):
    template_name = 'ksiazkaadresowa/contact.csv'

    def get_context_data(self, **kwargs):
        return {
            'contacts': Person.objects.all()
        }


class ContactJSON(View):
    def get(self, request, **kwargs):
        p = Person.objects.all().values()
        return JsonResponse(status=HTTPStatus.OK, data=list(p), safe=False)

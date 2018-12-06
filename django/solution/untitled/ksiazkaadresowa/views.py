from http import HTTPStatus
from django.http import JsonResponse
from django.views.generic import TemplateView, View, FormView
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


from .forms import PersonForm
from django.views.generic import FormView


class ContactCreate(FormView):
    template_name = 'ksiazkaadresowa/create.html'
    form_class = PersonForm
    success_url = '/contact.html'

    def form_valid(self, form):
        Person.objects.create(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
        )
        return super().form_valid(form)

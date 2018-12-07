import base64
from http import HTTPStatus

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.views.generic import TemplateView, View, FormView

from ksiazkaadresowa.forms import ContactCreateForm, ContactUsForm
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
        contacts = Person.objects.all()
        contacts = contacts.filter(last_name__startswith='T')
        return locals()


class BasicAuth:
    def basic_auth(self):
        auth_header = self.request.environ.get('HTTP_AUTHORIZATION', None)

        if not auth_header:
            raise PermissionError

        auth_type, credentials = auth_header.split()
        credentials = base64.b64decode(credentials).decode()
        username, password = credentials.split(':')

        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)
        else:
            raise PermissionError


class ContactJSON(BasicAuth, PermissionRequiredMixin, View):
    permission_required = 'mna.can_view'

    def dispatch(self, request, *args, **kwargs):
        try:
            self.basic_auth()
        except PermissionError:
            return JsonResponse(status=HTTPStatus.FORBIDDEN, data={
                'status': HTTPStatus.FORBIDDEN,
                'reason': 'Forbidden',
            })

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, **kwargs):
        p = Person.objects.all().values()
        return JsonResponse(status=HTTPStatus.OK, data=list(p), safe=False)


class ContactCreateView(FormView):
    template_name = 'ksiazkaadresowa/contact-create.html'
    form_class = ContactCreateForm
    success_url = '/contact.html'

    def form_valid(self, form):
        Person.objects.create(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
        )
        return super().form_valid(form)


class ContactUsView(FormView):
    template_name = 'ksiazkaadresowa/contact-form.html'
    form_class = ContactUsForm
    success_url = '/thank-you.html'


class ThankYouView(TemplateView):
    template_name = 'ksiazkaadresowa/thank-you.html'

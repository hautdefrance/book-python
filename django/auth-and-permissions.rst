********************
Auth and Permissions
********************


Basic Auth
==========
.. code-block:: python

    from django.contrib.auth import authenticate, login

    class BasicAuthMixin:
        def basic_auth(self):
            auth_header = self.request.META.get('HTTP_AUTHORIZATION')

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


    class ContactJSON(BasicAuthMixin, View):
        def get(self, request, **kwargs):
            if not request.user.is_authenticated:
                try:
                    self.basic_auth()
                except PermissionError:
                    return JsonResponse(status=HTTPStatus.FORBIDDEN, data={'status': HTTPStatus.FORBIDDEN, 'reason': 'Forbidden'})

            p = Person.objects.all().values()
            return JsonResponse(status=HTTPStatus.OK, data=list(p), safe=False)


Require Permissions
===================
.. code-block:: python

    from django.contrib.auth.mixins import PermissionRequiredMixin


    class ContactJSON(PermissionRequiredMixin, View):
        permission_required = 'contact.can_view'

        def get(self, request, **kwargs):
            p = Person.objects.all().values()
            return JsonResponse(status=HTTPStatus.OK, data=list(p), safe=False)


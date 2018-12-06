from django.conf import settings
from django.contrib import admin
from django.urls import path

from mna.views import RedirectAPIv1, RedirectAPIv2
from ksiazkaadresowa.views import ContactHTML, ContactCSV, ContactJSON, ContactCreate


urlpatterns = [
    path('admin/', admin.site.urls),

    # path('contact/<str:last_name>/', ContactHTML.as_view()),
    path('contact/create/', ContactCreate.as_view()),
    path('contact.csv', ContactCSV.as_view()),
    path('contact.json', ContactJSON.as_view()),
    path('contact.html', ContactHTML.as_view()),

    path('api/v1/redirect/', RedirectAPIv1.as_view()),
    path('api/v2/redirect/', RedirectAPIv2.as_view()),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

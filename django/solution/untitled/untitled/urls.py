from django.conf import settings
from django.contrib import admin
from django.urls import path

from mna.views import RedirectAPIv1, RedirectAPIv2
from ksiazkaadresowa.views import ContactView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('contact/<str:last_name>/', ContactView.as_view()),
    path('contact/', ContactView.as_view()),

    path('api/v1/redirect/', RedirectAPIv1.as_view()),
    path('api/v2/redirect/', RedirectAPIv2.as_view()),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

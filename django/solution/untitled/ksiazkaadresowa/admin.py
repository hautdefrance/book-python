from django.contrib import admin
from .models import Person, Address


class AddressInline(admin.TabularInline):
    model = Address
    extra = 0
    max_num = 4
    min_num = 0


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'date_of_birth']
    search_fields = ['^last_name']
    ordering = ['last_name']
    autocomplete_fields = ['friends']
    inlines = [AddressInline]
    readonly_fields = ['id']
    exclude = ['is_deleted']
    list_per_page = 100

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = self.readonly_fields

        if not request.user.is_superuser:
            return readonly_fields + ['first_name', 'last_name', 'phone', 'date_of_birth']
        else:
            return readonly_fields

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if not request.user.is_superuser:
            qs = qs.filter(is_deleted=False)

        return qs

    class Media:
        js = [
            'ksiazkaadresowa/js/admin-person.js',
        ]

        css = {'all': [
            'ksiazkaadresowa/css/admin-person.css',
        ]}


#@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['person', 'street', 'house_number', 'apartment_number', 'city', 'region', 'country']
    search_fields = ['^street', '^city']
    autocomplete_fields = ['person']
    ordering = ['person', 'street']

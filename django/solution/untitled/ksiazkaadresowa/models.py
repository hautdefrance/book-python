from django.db import models
from django.utils.translation import ugettext_lazy as _


class Person(models.Model):
    is_deleted = models.BooleanField(verbose_name=_('Is Deleted?'), default=False)

    first_name = models.CharField(verbose_name=_('First Name'), max_length=30)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=30, db_index=True)
    phone = models.IntegerField(verbose_name=_('Phone'), null=True, blank=True)
    date_of_birth = models.DateField(verbose_name=_('Date of birth'), null=True, blank=True)
    image = models.ImageField(verbose_name=_('Image'), upload_to='person/', null=True, blank=True)
    friends = models.ManyToManyField(verbose_name=_('Friends'), to='ksiazkaadresowa.Person', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('People')
        unique_together = ['first_name', 'last_name']


class Address(models.Model):
    person = models.ForeignKey(verbose_name=_('Person'), to='ksiazkaadresowa.Person', on_delete=models.CASCADE)
    street = models.CharField(verbose_name=_('Street'), max_length=30, db_index=True)
    house_number = models.CharField(verbose_name=_('House Number'), max_length=5)
    apartment_number = models.CharField(verbose_name=_('Apartment Number'), max_length=5, null=True, blank=True)
    city = models.CharField(verbose_name=_('City'), max_length=30, null=True, blank=True, db_index=True)
    post_code = models.IntegerField(verbose_name=_('Post Code'), null=True, blank=True)
    region = models.CharField(verbose_name=_('Region'), max_length=30, null=True, blank=True)
    country = models.CharField(verbose_name=_('Country'), max_length=30, null=True, blank=True)

    def __str__(self):
        return f'{self.street}, {self.city}'

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')


from datetime import date
from django import template
from django.utils.translation import ugettext_lazy as _


register = template.Library()
AGE_ADULT = 18 * 365


@register.simple_tag
def czy_pelnoletni(contact):

    if contact.is_adult() is None:
        return ''

    if contact.is_adult():
        return _('Adult')
    else:
        return _('Kid')

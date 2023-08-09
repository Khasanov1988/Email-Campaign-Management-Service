from django import template
from django.utils.safestring import mark_safe

register = template.Library()


# Создание тега
@register.simple_tag
def mediapath(format_string):
    return f'/media/{format_string}'


# Создание фильтра
@register.filter
def mediapath_filter(text):
    return f'/media/{text}'

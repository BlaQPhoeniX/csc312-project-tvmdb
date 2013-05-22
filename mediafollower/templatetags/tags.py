from django import template
import re
import datetime

register = template.Library()

@register.simple_tag
def navactive(request, pattern):
    if re.search(pattern, request.path):
        return 'active'
    return ''


def age(bday, d=None):
    if not d:
        d = datetime.date.today()
    return (d.year - bday.year) - int((d.month, d.day) < (bday.month, bday.day))

register.filter('age', age)

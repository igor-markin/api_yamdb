from django.core.exceptions import ValidationError
from django.utils import timezone


def year_validator(value):
    if value > timezone.now().year:
        params = {'value': value, }
        raise ValidationError('Год больше текущего', params=params)

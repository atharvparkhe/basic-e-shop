from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_stars(value):
    try:
        return round(float(value), 2)
    except:
        raise ValidationError(
            _('%(value)s is not an integer or a float  number'),
            params={'value': value},
        )
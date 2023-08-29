from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_min_length(value):
    if len(value) < 11:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )
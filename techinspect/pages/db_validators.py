from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from datetime import datetime #For validate_car_year


def validate_car_year(value):
    if value > datetime.now().year + 1:
        raise ValidationError(
        _('The year value %(value) cannot be more than %(acceptable_year)'),
        params={'value': value, 'acceptable_year': datetime.now().year + 1},

        )


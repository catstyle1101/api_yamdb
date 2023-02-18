from datetime import datetime

from django.conf import settings
from django.core.exceptions import ValidationError


def year_validator(year: int) -> None:
    current_date = datetime.today().year
    if year > current_date:
        raise ValidationError(f"Year value {year} is not valid")


def rating_validator(rating) -> None:
    if not (settings.MIN_RATING <= int(rating) <= settings.MAX_RATING):
        raise ValidationError(f"Rating value {rating} is not valid")

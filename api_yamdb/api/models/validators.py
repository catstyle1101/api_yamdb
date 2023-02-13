import datetime
from django.conf import settings
from django.core.exceptions import ValidationError


def rating_validator(rating: int) -> bool:
    if rating < 0 or rating > settings.MAX_RATING:
        raise ValidationError(f"Rating value {rating} is not valid")


def year_validator(year: int) -> bool:
    current_date = datetime.date.today().year
    if year > current_date:
        raise ValidationError(f"Year value {year} is not valid")

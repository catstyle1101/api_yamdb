from django.conf import settings
from django.core.exceptions import ValidationError


def rating_validator(rating: int) -> bool:
    if not rating < 0 or rating > settings.MAX_RATING:
        raise ValidationError(f"Rating value {rating} is not valid")

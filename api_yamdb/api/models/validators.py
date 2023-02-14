import datetime
from django.core.exceptions import ValidationError


def year_validator(year: int) -> bool:
    current_date = datetime.date.today().year
    if year > current_date:
        raise ValidationError(f"Year value {year} is not valid")

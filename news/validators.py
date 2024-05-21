from django.core.exceptions import ValidationError


def validate_category_name(value):
    if len(value) == 0 or len(value) < 200:
        raise ValidationError("Invalid category name.")

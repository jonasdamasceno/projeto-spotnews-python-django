from django.core.exceptions import ValidationError


def validate_category_length(value):
    if len(value) == 0 or len(value) < 200:
        raise ValidationError("Invalid category name.")
    elif len(value) > 200:
        raise ValidationError(
            f"tamanho maximo 200 caracteres(tem {len(value)})."
        )

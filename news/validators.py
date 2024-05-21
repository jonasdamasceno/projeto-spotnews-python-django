from django.core.exceptions import ValidationError


def validate_category_length(value):
    if len(value) == 0:
        raise ValidationError("Este campo não pode estar vazio.")
    elif len(value) > 200:
        raise ValidationError(
            f"Certifique-se de que o valor tenha no máximo 200 caracteres (ele possui {len(value)})."  # noqa
        )

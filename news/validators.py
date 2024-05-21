from django.core.exceptions import ValidationError


def validate_empty_data(value):
    if len(value) == 0:
        raise ValidationError("Este campo não pode estar vazio.")


def validate_max_length(value):
    if len(value) > 200:
        raise ValidationError(
            f"Certifique-se de que o valor tenha no máximo 200 caracteres (ele possui {len(value)})."  # noqa
        )


def validate_title_length(value):
    if len(value.split()) == 1:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")


def validate_date_format(value):
    if not value.strftime("%Y-%m-%d"):
        raise ValidationError(
            f"O valor {value} tem um formato de data inválido. Deve ser no formato  YYYY-MM-DD."  # noqa
        )

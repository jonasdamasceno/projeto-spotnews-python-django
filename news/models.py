from django.db import models
from news.validators import (
    validate_empty_data,
    validate_max_length,
    validate_title_length,
    validate_date_format,
)


class Category(models.Model):
    name = models.CharField(
        max_length=200, validators=[validate_empty_data, validate_max_length]
    )

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(
        max_length=200, validators=[validate_empty_data, validate_max_length]
    )
    email = models.EmailField(
        max_length=200, validators=[validate_empty_data, validate_max_length]
    )
    password = models.CharField(
        max_length=200, validators=[validate_empty_data, validate_max_length]
    )
    role = models.CharField(
        max_length=200, validators=[validate_empty_data, validate_max_length]
    )

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[
            validate_empty_data,
            validate_max_length,
            validate_title_length,
        ],
    )
    content = models.TextField(validators=[validate_empty_data])
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="news"
    )
    created_at = models.DateField(validators=[validate_date_format])
    image = models.ImageField(upload_to="img/", null=True, blank=True)
    categories = models.ManyToManyField(
        Category, related_name="news", validators=[validate_empty_data]
    )

    def __str__(self) -> str:
        return self.title

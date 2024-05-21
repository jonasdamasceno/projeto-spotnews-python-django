from django.db import models
from news.validators import validate_category_length


class Category(models.Model):
    name = models.CharField(
        max_length=200, validators=[validate_category_length]
    )

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(
        max_length=200, validators=[validate_category_length]
    )
    email = models.EmailField(
        max_length=200, validators=[validate_category_length]
    )
    password = models.CharField(
        max_length=200, validators=[validate_category_length]
    )
    role = models.CharField(
        max_length=200, validators=[validate_category_length]
    )

    def __str__(self):
        return self.name

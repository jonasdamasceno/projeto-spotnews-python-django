from django.db import models
from news.validators import validate_category_name


class Category(models.Model):
    name = models.CharField(
        max_length=200, validators=[validate_category_name]
    )

    def __str__(self):
        return self.name

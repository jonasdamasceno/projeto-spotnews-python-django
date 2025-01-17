from django.db import models
from django.utils import timezone
from news.validators import (
    validate_empty,
    validate_max_length,
    validate_title_length,
    validate_date,
)


class Category(models.Model):
    name = models.CharField(
        max_length=200, validators=[validate_empty, validate_max_length]
    )

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(
        max_length=200,
        validators=[validate_empty, validate_max_length],
        verbose_name="Nome",
    )
    email = models.EmailField(
        max_length=200,
        validators=[validate_empty, validate_max_length],
        unique=True,
        verbose_name="Email",
    )
    password = models.CharField(
        max_length=200,
        validators=[validate_empty, validate_max_length],
        verbose_name="Senha",
    )
    role = models.CharField(
        max_length=200,
        validators=[validate_empty, validate_max_length],
        verbose_name="Função",
    )

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[
            validate_empty,
            validate_max_length,
            validate_title_length,
        ],
    )
    content = models.TextField(validators=[validate_empty])
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="news"
    )
    created_at = models.DateField(
        default=timezone.now, validators=[validate_date]
    )
    image = models.ImageField(upload_to="img/", null=True, blank=True)
    categories = models.ManyToManyField(
        Category, related_name="news", validators=[validate_empty]
    )

    def __str__(self) -> str:
        return self.title

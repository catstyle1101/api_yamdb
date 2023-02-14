from django.db import models
from api.models.categories import Categories
from api.models.validators import year_validator


class Titles(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название',
    )
    year = models.IntegerField(validators=(year_validator,))
    description = models.TextField(
        verbose_name='Описание',
        blank=True)
    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        null=True,
        related_name='title',
        verbose_name='Категория',
    )

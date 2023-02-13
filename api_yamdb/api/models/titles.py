from django.db import models
from .categories import Categories
from .genres import GenreCategories, Genre
from .validators import rating_validator, year_validator


class Titles(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название',
    )
    year = models.IntegerField(validators=(year_validator,))
    rating = models.IntegerField(validators=(rating_validator,))
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
    genre = models.ManyToManyField(
        Genre,
        through='GenreCategories',
        verbose_name='Жанр',
    )

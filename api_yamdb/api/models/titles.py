from django.db import models
from .categories import Categories
from .genres import Genre
from .validators import year_validator


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
    genre = models.ManyToManyField(Genre, through='GenreCategories')


class GenreCategories(models.Model):
    title_id = models.ForeignKey(
        Titles,
        on_delete=models.CASCADE
    )
    genre_id = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title_id', 'genre_id'],
                name='unique_title_genre'
            )
        ]

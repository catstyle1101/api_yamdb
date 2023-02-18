from django.db import models
from .categories import Categories
from .genres import Genre
from .validators import year_validator


class Title(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название',
    )
    year = models.PositiveSmallIntegerField(validators=(year_validator,))
    description = models.TextField(
        verbose_name='Описание',
        blank=True)
    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='category',
        verbose_name='Категория',
    )
    genre = models.ManyToManyField(
        'Genre',
        through='GenreCategories',
        related_name='genre',
        verbose_name='Жанр',
    )


class GenreCategories(models.Model):
    title_id = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
    )
    genre_id = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title_id', 'genre_id'],
                name='unique_title_genre'
            )
        ]

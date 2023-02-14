from django.db import models
from .titles import Titles


class Genre(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название',
        unique=True,
    )
    slug = models.SlugField(
        unique=True,
        max_length=50,
        verbose_name='Слаг'
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


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

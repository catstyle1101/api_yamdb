from django.db import models


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

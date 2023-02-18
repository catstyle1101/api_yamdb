from django.db import models


class Categories(models.Model):
    name = models.CharField(
        'Название',
        max_length=256,
        unique=True,
    )
    slug = models.SlugField(
        'Слаг',
        unique=True,
        max_length=50,
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

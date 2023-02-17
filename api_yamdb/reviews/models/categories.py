from django.db import models


class Categories(models.Model):
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
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

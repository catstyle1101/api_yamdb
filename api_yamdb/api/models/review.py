from django.db import models

from api.titles import Titles
from api.users import User
from api.validators import rating_validator


class Review(models.Model):
    title_id = models.ForeignKey(
        Titles,
        on_delete=models.CASCADE,
        related_name='review',
        verbose_name='Отзыв',
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author',
        verbose_name='Автор отзыва',
    )
    score = models.IntegerField(validators=(rating_validator,))

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text

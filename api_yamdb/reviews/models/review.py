from django.db import models

from .title import Title
from core.models.users import User
from .validators import rating_validator


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Отзыв',
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='review_author',
        verbose_name='Автор отзыва',
    )
    score = models.PositiveSmallIntegerField(validators=(rating_validator,))
    pub_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_title_author_review'
            )
        ]

    def __str__(self):
        return self.text

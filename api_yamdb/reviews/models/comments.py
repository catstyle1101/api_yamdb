from django.db import models

from .review import Review
from core.models.users import User


class Comments(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Коментарии',
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comment_author',
        verbose_name='Автор комментария',
    )
    pub_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Коментариев'

    def __str__(self):
        return self.text

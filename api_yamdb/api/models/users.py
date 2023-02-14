from django.db import models

class Users(models.Model):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLE_CHOICES = (
        (USER, 'Аутентифицированный пользователь'),
        (ADMIN, 'Администратор'),
        (MODERATOR, 'Модератор')
    )
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=150,
        null=False,
        unique=True
    )
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        unique=True,
        max_length=254
    )
    role = models.CharField(
        verbose_name='Роль',
        max_length=50,
        choices=ROLE_CHOICES,
        default=USER
    )
    bio = models.TextField(
        'Биография',
        null=True,
        blank=True,
    )


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username 
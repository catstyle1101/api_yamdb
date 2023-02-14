from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_CHOICES = (
    ("ADMIN", "admin"),
    ("USER", "user"),
    ("MODERATOR", "moderator"),
)


class User(AbstractUser):
    email = models.EmailField(
        unique=True, db_index=True, verbose_name="Электронная почта"
    )
    bio = models.TextField(blank=True, verbose_name="О себе")
    role = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES,
        default="USER",
        verbose_name="Роль",
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    @property
    def is_user(self):
        return self.role == "user"

    @property
    def is_admin(self):
        return self.role == "admin"

    @property
    def is_moderator(self):
        return self.role == "moderator"

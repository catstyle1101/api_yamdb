from django.db import models

class Users(models.Model):
    username = models.CharField(
        max_length=200
    )
    email = models.EmailField(
        ('email address'),
        unique=True)
    
    # role = models.CharField(max_length=300, choices = CHOICES)
    # не понял как это реализовывать
    bio = models.TextField(
        max_length=500,
        blank=True)
    first_name = models.CharField(
        ('first name'),
        max_length=100,
        blank=True
    )
    last_name = models.CharField(
        ('last name'),
        max_length=100,
        blank=True
    )


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username 
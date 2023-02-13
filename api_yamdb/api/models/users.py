from django.db import models

class Users(models.Model):
    username = models.CharField(
        max_length=200
    )
    email = models.EmailField(
        ('email address'),
        unique=True)
    
    bio = models.TextField(
        max_length=500,
        blank=True)
    first_name = models.CharField(
        ('first name'),
        max_length=30,
        blank=True
    )
    last_name = models.CharField(
        ('last name'),
        max_length=30,
        blank=True
    )


from django.contrib.auth.models import AbstractUser
from django.db import models

#creating custom user and registering it in settings.py: AUTH_USER_MODEL = 'accounts.User'
class User(AbstractUser):
    ROLE_CHOICES = (
        ('owner', 'Owner'),
        ('manager', 'Manager'),
        ('sales', 'Sales'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.role})"

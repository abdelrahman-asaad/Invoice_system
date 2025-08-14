from django.db import models
from common.models import BaseModel  # لو عايز تورث BaseModel

class Product(BaseModel):
    CURRENCY_CHOICES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('EGP', 'Egyptian Pound'),
    ]

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='USD')

    def __str__(self):
        return self.name

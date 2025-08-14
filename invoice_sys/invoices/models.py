from django.db import models
from common.models import BaseModel
from clients.models import Client
from products.models import Product
from django.conf import settings

class Invoice(BaseModel):
    STATUS_CHOICES = (
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
        ('overdue', 'Overdue'),
    )

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='invoices')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='invoices')
    date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Invoice #{self.id} - {self.client.name}"

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

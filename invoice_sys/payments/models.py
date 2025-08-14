from django.db import models
from invoices.models import Invoice

class Payment(models.Model):
    METHOD_CHOICES = (
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('bank', 'Bank Transfer'),
    )

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='payments')
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=20, choices=METHOD_CHOICES)

    def __str__(self):
        return f"Payment for Invoice #{self.invoice.id}"

# to update Invoice.total_amount when adding/deleting/modifying InvoiceItem
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import InvoiceItem, Invoice

def update_invoice_total(invoice):
    total = sum(item.total_price for item in invoice.items.all()) #check line 25 in modles.py
    invoice.total_amount = total           #related name='items' while invoice is field
    invoice.save()


@receiver(post_save, sender=InvoiceItem)
def update_total_on_save(sender, instance, **kwargs): #for handling add item in invoice
    update_invoice_total(instance.invoice)


@receiver(post_delete, sender=InvoiceItem)          #for handling delete item in invoice
def update_total_on_delete(sender, instance, **kwargs):
    update_invoice_total(instance.invoice)

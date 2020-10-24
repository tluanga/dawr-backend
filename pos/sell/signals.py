from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SettleBill, Order

@receiver(post_save, sender=Order)
def post_save_create_bill(sender, instance, created, **kwargs):
    if created:
        print('sender', sender)
        print('instance', instance)
        print('created', created)
        SettleBill.objects.create(order=instance)


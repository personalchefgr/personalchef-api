from django.db import models

from users.models import CustomUser
from dietary_plans.models import DietaryPlan
from subscriptions.models import Subscription

PAYMENT_STATUS_CHOICES = [
        ('pending', 'Εκκρεμεί'),
        ('aborted', 'Ακυρώθηκε'),
        ('completed', 'Ολοκληρώθηκε'),
]

class Order(models.Model):
    user = models.ForeignKey(CustomUser, related_name='user', on_delete=models.CASCADE)

    dietary_plan = models.ForeignKey(DietaryPlan, related_name='dietary_plan', on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, related_name='subscription', on_delete=models.CASCADE)

    days = models.JSONField()
    start_date = models.DateField()

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(choices=PAYMENT_STATUS_CHOICES, max_length=25)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ('Order %s - %s - %s' % (self.id, self.user, self.created_at))

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    
from django.db import models

from users.models import CustomUser
from dietary_plans.models import DietaryPlan
from subscriptions.models import Subscription


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    dietary_plan = models.ForeignKey(DietaryPlan, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    days = models.JSONField()
    start_date = models.DateField()

    payment = models.CharField(max_length=25)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return ('Order %s - %s - %s' % (self.id, self.user, self.created_at))
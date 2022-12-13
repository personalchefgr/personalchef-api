from django.db import models

from dietary_plans.models import DietaryPlan
from subscriptions.models import Subscription


class PricingPlan(models.Model):
        dietary_plan = models.ForeignKey(DietaryPlan,
                                        on_delete=models.CASCADE)

        subscription = models.ForeignKey(Subscription,
                                        on_delete=models.CASCADE)


        slug = models.CharField(max_length=250)

        price_per_meal = models.DecimalField(
                                        max_digits=10,
                                        decimal_places=2,
                                        blank=True)

        sort_order = models.PositiveIntegerField()

        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
                return ("%s - %s" % (self.dietary_plan, self.subscription))

        class Meta:
                db_table = "pricing_plans"
                ordering = ['sort_order']
                verbose_name = "Pricing Plan"
                verbose_name_plural = "Pricing Plans"

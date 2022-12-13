from rest_framework import serializers

from . import models
from dietary_plans.serializers import DietaryPlanListSerializer
from subscriptions.serializers import SubscriptionSerializer

class PricingPlanSerializer(serializers.ModelSerializer):
    dietary_plan = DietaryPlanListSerializer(read_only=True)
    subscription = SubscriptionSerializer(read_only=True)

    class Meta:
        model = models.PricingPlan
        fields = [
            'slug',
            'dietary_plan', 
            'subscription', 
            'price_per_meal'
        ]
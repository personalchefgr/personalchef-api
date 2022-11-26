from rest_framework import serializers

from . import models

class PricingPlanListSerializer(serializers.ModelSerializer):
    dietary_plan = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    subscription = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = models.PricingPlan
        fields = ['dietary_plan', 'subscription', 'price']
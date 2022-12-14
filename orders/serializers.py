import random

from rest_framework import serializers

from . import models

from users.models import CustomUser
from dietary_plans.models import DietaryPlan
from subscriptions.models import Subscription

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=CustomUser.objects.all(), 
        slug_field='email')
    
    dietary_plan = serializers.SlugRelatedField(
        queryset=DietaryPlan.objects.all(), 
        slug_field='slug')

    subscription = serializers.SlugRelatedField(
        queryset=Subscription.objects.all(), 
        slug_field='slug')

    class Meta:
        model = models.Order
        fields = [
            'user', 
            'dietary_plan', 
            'subscription',
            'days',
            'start_date',
            'total_amount',
            'payment_status'
        ]
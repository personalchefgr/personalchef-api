from rest_framework.serializers import ModelSerializer

from . import models

class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = models.Subscription
        fields = [
            'name', 
            'slug', 
            'duration', 
            'meals_per_day',
            'number_of_weeks',
            ]
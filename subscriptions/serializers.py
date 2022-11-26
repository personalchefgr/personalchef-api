from rest_framework.serializers import ModelSerializer

from . import models

class SubscriptionListSerializer(ModelSerializer):
    class Meta:
        model = models.Subscription
        fields = ['name', 'slug', 'duration']
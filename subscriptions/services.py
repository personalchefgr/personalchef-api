from rest_framework.response import Response
from rest_framework import status

from . import models, serializers

class SubscriptionService:
    @staticmethod
    def get_all():
        subscriptions = models.Subscription.objects.all()
        
        serializer = serializers.SubscriptionSerializer(
            subscriptions, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
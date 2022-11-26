from . import models, serializers

class SubscriptionService:
    @staticmethod
    def get_all_subscriptions():
        subscriptions = models.Subscription.objects.all()
        serializer = serializers.SubscriptionListSerializer(subscriptions, many=True)

        return serializer.data
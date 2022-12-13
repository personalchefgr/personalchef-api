from rest_framework.response import Response
from rest_framework import status

from . import models, serializers

class PricingPlanService:
    @staticmethod
    def get_all(dietary_plan=None):
        if dietary_plan is not None:
            subscriptions = models.PricingPlan.objects.filter(
                dietary_plan=dietary_plan)
        else: 
            subscriptions = models.PricingPlan.objects.all()
        
        serializer = serializers.PricingPlanListSerializer(
            subscriptions, many=True)

        return Response(serializer.data, 
                status=status.HTTP_200_OK)
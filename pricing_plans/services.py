from rest_framework.response import Response
from rest_framework import status

from . import models, serializers

class PricingPlanService:
    @staticmethod
    def get_all(dietary_plan=None):
        if dietary_plan is not None:
            pricing_plans = models.PricingPlan.objects.filter(
                dietary_plan__slug=dietary_plan)
        else: 
            pricing_plans = models.PricingPlan.objects.all()
        
        serializer = serializers.PricingPlanSerializer(
            pricing_plans, many=True)

        return Response(serializer.data, 
                status=status.HTTP_200_OK)
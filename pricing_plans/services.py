from . import models, serializers

class PricingPlanService:
    @staticmethod
    def get_all_pricing_plans():
        pricing_plans = models.PricingPlan.objects.all()
        serializer = serializers.PricingPlanListSerializer(pricing_plans, many=True)

        return serializer.data
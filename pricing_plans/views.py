from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from . import services

class PricingPlanList(APIView):
    def get(self, request):
        pricing_plans = services.PricingPlanService.get_all_pricing_plans()

        return Response(pricing_plans, status=HTTP_200_OK)
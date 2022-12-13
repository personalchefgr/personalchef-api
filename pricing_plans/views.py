from rest_framework.views import APIView

from .services import PricingPlanService

class PricingPlanList(APIView):
    permission_classes = []

    def get(self, request):
        dietary_plan = request.query_params.get('dietary_plan')
        
        response = PricingPlanService.get_all()

        return response
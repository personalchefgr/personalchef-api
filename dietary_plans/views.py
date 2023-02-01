from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .services import DietaryPlanService, MealService

class DietaryPlanList(APIView):
    permission_classes = []

    def get(self, request):
        response = DietaryPlanService.get_all()

        return response


class DietaryPlanDetails(APIView):
    permission_classes = []

    def get(self, request, slug):
        response = DietaryPlanService.get_dietary_plan_by_slug(slug)
        
        return response


class MealList(APIView):
    permission_classes = []
    
    def get(self, request):
        response = MealService.get_all(request)

        return response


class MealDetails(APIView):
    permission_classes = []
    
    def get(self, request, slug):
        response = MealService.get_meal_by_slug(slug)
        
        return response
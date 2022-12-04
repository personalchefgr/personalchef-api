from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from . import services

class DietaryPlanList(APIView):
    def get(self, request):
        dietary_plans = services.DietaryPlanService.get_all_dietary_plans()

        return Response(dietary_plans, status=HTTP_200_OK)


class DietaryPlanDetails(APIView):
    def get(self, request, slug):
        dietary_plan = services.DietaryPlanService.get_dietary_plan_by_slug(slug)
        
        return Response(dietary_plan, status=HTTP_200_OK)


class MealList(APIView):
    permission_classes = []
    
    def get(self, request):
        dietary_plan_slug = request.query_params.get('dietary_plan_slug')
        
        if dietary_plan_slug is None:
            meals = services.DietaryPlanService.get_all_meals()
        else:
            meals = services.DietaryPlanService.get_meals_per_dietary_plan_by_slug(dietary_plan_slug)

        return Response(meals, status=HTTP_200_OK)


class MealDetails(APIView):
    permission_classes = []
    
    def get(self, request, slug):
        meal = services.DietaryPlanService.get_meal_by_slug(slug)
        
        return Response(meal, status=HTTP_200_OK)
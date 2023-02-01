from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response

from . import models, serializers

class DietaryPlanService:
    @staticmethod
    def get_all():
        dietary_plans = models.DietaryPlan.objects.all()
        serializer = serializers.DietaryPlanListSerializer(
                    dietary_plans, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def get_dietary_plan_by_slug(slug=None):
        dietary_plan = get_object_or_404(models.DietaryPlan, slug=slug)
        serializer = serializers.DietaryPlanDetailsSerializer(dietary_plan)

        return Response(serializer.data, status=status.HTTP_200_OK)


class MealService:
    @staticmethod
    def get_all(request):
        dietary_plan = request.query_params.get('dietary_plan')
        
        if dietary_plan is not None:
            meals = models.Meal.objects.filter(
                    dietary_plan=dietary_plan)
        else: 
            meals = models.Meal.objects.all()
        
        serializer = serializers.MealListSerializer(meals,
                    many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def get_meal_by_slug(slug=None):
        meal = get_object_or_404(models.Meal, slug=slug)
        serializer = serializers.MealDetailsSerializer(meal)

        return Response(serializer.data, status=status.HTTP_200_OK)
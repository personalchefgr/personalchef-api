from django.shortcuts import get_object_or_404

from . import models, serializers

class DietaryPlanService:
    @staticmethod
    def get_all_dietary_plans():
        dietary_plans = models.DietaryPlan.objects.all()
        serializer = serializers.DietaryPlanListSerializer(dietary_plans, many=True)

        return serializer.data

    @staticmethod
    def get_dietary_plan_by_slug(slug=None):
        dietary_plan = get_object_or_404(models.DietaryPlan, slug=slug)
        serializer = serializers.DietaryPlanDetailsSerializer(dietary_plan)

        return serializer.data

    @staticmethod
    def get_all_meals():
        meals = models.Meal.objects.all()
        serializer = serializers.MealListSerializer(meals, many=True)

        return serializer.data
    
    @staticmethod
    def get_meals_per_dietary_plan_by_slug(dietary_plan_slug=None):
        meals = models.Meal.objects.filter(dietaryplan__slug=dietary_plan_slug)
        serializer = serializers.MealListSerializer(meals, many=True)

        return serializer.data

    @staticmethod
    def get_meal_by_slug(slug=None):
        meal = get_object_or_404(models.Meal, slug=slug)
        serializer = serializers.MealDetailsSerializer(meal)

        return serializer.data
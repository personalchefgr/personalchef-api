from rest_framework import serializers

from . import models

class DietaryPlanListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DietaryPlan
        fields = ["name", "slug", "snippet", "img"]


class DietaryPlanDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DietaryPlan
        fields = "__all__"


class MealNutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MealNutrition
        fields = ['calories', 'protein', 'carbs', 'fat']


class MealListSerializer(serializers.ModelSerializer):
    plans = serializers.SlugRelatedField(
        many=True, 
        read_only=True, 
        slug_field='slug')
        
    nutrition = MealNutritionSerializer(read_only=True)

    class Meta:
        model = models.Meal
        fields = ['name', 'slug', 'img', 'plans', 'nutrition']


class MealDetailsSerializer(serializers.ModelSerializer):
    nutrition = MealNutritionSerializer(read_only=True)
    
    class Meta:
        model = models.Meal
        fields = "__all__"
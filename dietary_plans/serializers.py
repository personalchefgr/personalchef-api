from rest_framework import serializers

from . import models

class DietaryPlanListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DietaryPlan
        fields = ["name", "slug", "description"]


class DietaryPlanDetailsSerializer(serializers.ModelSerializer):
    meals = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='slug'
    )

    class Meta:
        model = models.DietaryPlan
        fields = "__all__"


class MealListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Meal
        fields = ['name', 'slug', 'calories', 'protein', 'carbs', 'fat']


class MealDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Meal
        fields = "__all__"

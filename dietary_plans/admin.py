from django.contrib import admin

from . import models

@admin.register(models.DietaryPlan)
class DietaryPlanAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Meal)
class MealAdmin(admin.ModelAdmin):
    pass

@admin.register(models.MealNutrition)
class MealNutritionAdmin(admin.ModelAdmin):
    pass
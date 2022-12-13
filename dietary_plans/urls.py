from django.urls import path

from . import views

app_name = "dietary_plans"
urlpatterns = [
    path('', 
        views.DietaryPlanList.as_view(), 
        name="dietary_plan-list"),

    path('dietary-plan/<slug:slug>', 
        views.DietaryPlanDetails.as_view(), 
        name="dietary_plan-details"),

    path('meals', 
        views.MealList.as_view(), 
        name="meal-list"),
        
    path('meals/meal/<slug:slug>', 
        views.MealDetails.as_view(), 
        name="meal-details"),
]
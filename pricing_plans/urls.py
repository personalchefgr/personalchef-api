from django.urls import path

from . import views

app_name="pricing_plans"
urlpatterns = [
    path("", views.PricingPlanList.as_view(), name="pricing_plan-list"),
]
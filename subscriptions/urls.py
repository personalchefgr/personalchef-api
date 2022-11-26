from django.urls import path

from . import views

app_name="subscriptions"
urlpatterns = [
    path('', views.SubscriptionList.as_view(), name="subscription-list"),
    path('<slug:slug>', views.SubscriptionDetails.as_view(), name="subscription-details"),
]
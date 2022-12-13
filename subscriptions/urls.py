from django.urls import path

from . import views

app_name="subscriptions"
urlpatterns = [
    path('', views.SubscriptionList.as_view(), name="subscription-list"),
]
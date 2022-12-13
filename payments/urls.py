from django.urls import path

from . import views

app_name="payments"
urlpatterns = [
    path("payment-order", views.PaymentOrderView.as_view(), name="payment-order")
]
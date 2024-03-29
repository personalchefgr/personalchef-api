from django.urls import path

from . import views

app_name="payments"
urlpatterns = [
    path("order/<int:order_id>", views.PaymentOrderView.as_view(), name="complete-payment"),
    path("confirm-payment", views.ConfirmPaymentView.as_view(), name="confirm-payment"),
]
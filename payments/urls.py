from django.urls import path

from . import views

app_name="payments"
urlpatterns = [
    path("payment-order", views.PaymentOrderView.as_view(), name="payment-order"),
    path("verify-transaction", views.VerifyTransactionVIew.as_view(), name="verify-transaction"),
    path("confirm-payment", views.ConfirmPaymentView.as_view(), name="confirm-payment"),
]
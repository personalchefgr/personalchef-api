from django.urls import path

from . import views

app_name="orders"
urlpatterns = [
    path('create-order', views.NewOrderView.as_view(), name="create-order"),
    path('order/<int:id>', views.OrderView.as_view(), name="order"),
    path('order/<int:id>/shipping-details', views.OrderShippingDetailsView.as_view(), name="order-shipping-details"),
    path('order/<int:id>/billing-details', views.OrderBillingDetailsView.as_view(), name="order-billing-details"),
    path('order/<int:id>/company-tax-details', views.OrderCompanyTaxDetailsView.as_view(), name="order-company-tax-details"),
]

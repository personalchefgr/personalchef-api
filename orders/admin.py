from django.contrib import admin

from . import models

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(models.OrderShippingDetails)
class OrderShippingDetailsAdmin(admin.ModelAdmin):
    pass

@admin.register(models.OrderBillingDetails)
class OrderBillingDetailsAdmin(admin.ModelAdmin):
    pass

@admin.register(models.OrderCompanyTaxDetails)
class OrderCompanyTaxDetailsAdmin(admin.ModelAdmin):
    pass


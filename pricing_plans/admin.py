from django.contrib import admin

from . import models

@admin.register(models.PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    pass

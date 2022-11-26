from django.contrib import admin

from . import models

@admin.register(models.Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    pass

@admin.register(models.MealOption)
class MealOptionAdmin(admin.ModelAdmin):
    pass

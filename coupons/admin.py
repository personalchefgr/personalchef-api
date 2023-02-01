from django.contrib import admin

from . import models

@admin.register(models.Coupon)
class CouponAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CouponDiscount)
class CouponDiscountAdmin(admin.ModelAdmin):
    pass

@admin.register(models.CouponUser)
class CouponUserAdmin(admin.ModelAdmin):
    pass


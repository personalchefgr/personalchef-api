from rest_framework import serializers

from . import models

class CouponDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CouponDiscount
        fields = ['value', 'is_percentage']

class CouponSerializer(serializers.ModelSerializer):
    discount = CouponDiscountSerializer(read_only=True)

    class Meta:
        model = models.Coupon
        fields = ['code', 'is_active', 'discount']
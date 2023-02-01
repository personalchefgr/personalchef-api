from rest_framework import serializers

from . import models

from users.models import CustomUser
from dietary_plans.models import DietaryPlan
from subscriptions.models import Subscription
from coupons.models import Coupon

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=CustomUser.objects.all(), 
        slug_field='email')
    
    dietary_plan = serializers.SlugRelatedField(
        queryset=DietaryPlan.objects.all(), 
        slug_field='slug')

    subscription = serializers.SlugRelatedField(
        queryset=Subscription.objects.all(), 
        slug_field='slug')

    coupon = serializers.SlugRelatedField(
        queryset=Coupon.objects.all(),
        slug_field='code',
        required=False,
        allow_null=True)

    class Meta:
        model = models.Order
        fields = "__all__"


class OrderShippingDetailsSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(
        queryset=models.OrderShippingDetails.objects.all())

    class Meta:
        model = models.OrderShippingDetails
        fields = "__all__"


class OrderBillingDetailsSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(
        queryset=models.OrderBillingDetails.objects.all())

    class Meta:
        model = models.OrderBillingDetails
        fields = "__all__"


class OrderCompanyTaxDetailsSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(
        queryset=models.OrderCompanyTaxDetails.objects.all(),
        pk_field='id')

    class Meta:
        model = models.OrderCompanyTaxDetails
        fields = "__all__"
from django.db import models

from users.models import CustomUser

class CouponUser(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    coupon = models.ForeignKey('Coupon', on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.user, self.coupon)

    class Meta:
        db_table = 'coupon_users'
        verbose_name = "User Coupon"
        verbose_name_plural = "User Coupons"


class CouponDiscount(models.Model):
    value = models.IntegerField()
    is_percentage = models.BooleanField(default=True)

    def __str__(self):
        if self.is_percentage:
            return "-{0}%".format(self.value)

        return "-{0}".format(self.value)
    
    class Meta:
        db_table = "coupon_discounts"
        verbose_name = "Coupon Discount"
        verbose_name_plural = "Coupon Discounts"


class Coupon(models.Model):
    code = models.CharField(max_length=25)
    discount = models.ForeignKey('CouponDiscount', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    times_used = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code
    
    class Meta:
        db_table = "coupons"
        verbose_name = "Coupon"
        verbose_name_plural = "Coupons"
from django.db import models

from users.models import CustomUser
from dietary_plans.models import DietaryPlan
from subscriptions.models import Subscription
from coupons.models import Coupon

INVOICE_TYPE_CHOICES = [
    ('receipt', 'Απόδειξη'),
    ('invoice', 'Τιμολόγιο'),
]

PAYMENT_METHOD_CHOICES = [
    ('online', 'Χρεωστική/Πιστωτική κάρτα'),
    ('physical', 'Αντικαταβολή'),
]

PAYMENT_STATUS_CHOICES = [
    ('pending', 'Εκκρεμεί'),
    ('aborted', 'Ακυρώθηκε'),
    ('completed', 'Ολοκληρώθηκε'),
]

class Order(models.Model):
    user = models.ForeignKey(CustomUser, related_name='user', on_delete=models.CASCADE)
    order_code = models.CharField(max_length=250, blank=True, default='')

    dietary_plan = models.ForeignKey(DietaryPlan, related_name='dietary_plan', on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, related_name='subscription', on_delete=models.CASCADE)

    days = models.JSONField()
    start_date = models.DateField()

    coupon = models.ForeignKey(Coupon, 
                            blank=True, 
                            null=True, 
                            related_name='order_coupon', 
                            on_delete=models.DO_NOTHING)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    final_amount = models.DecimalField(max_digits=10, decimal_places=2)

    invoice_type = models.CharField(choices=INVOICE_TYPE_CHOICES, max_length=30, default='receipt')
    payment_method = models.CharField(choices=PAYMENT_METHOD_CHOICES, max_length=30, default='online')
    payment_status = models.CharField(choices=PAYMENT_STATUS_CHOICES, max_length=30, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ('Order #%s - %s - %s' % (self.id, self.user, self.created_at.strftime("%d/%m/%Y")))

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderShippingDetails(models.Model):
    order = models.ForeignKey(Order, related_name='order_shipping_details', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    mobile_phone = models.CharField(max_length=15)
    landline_phone = models.CharField(max_length=15, blank=True)

    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True)
    address_number = models.PositiveIntegerField()
    town = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postcode = models.PositiveIntegerField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
    
    class Meta:
        db_table = "order_shipping_details"
        verbose_name = "Order - Shipping Details"
        verbose_name_plural = "Order - Shipping Details"


class OrderBillingDetails(models.Model):
    order = models.ForeignKey(Order, related_name='order_billing_details', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    mobile_phone = models.CharField(max_length=15)
    landline_phone = models.CharField(max_length=15, blank=True)

    address1 = models.CharField(max_length=255)
    address2 = models.CharField(
                max_length=255, 
                blank=True)
    address_number = models.PositiveIntegerField()
    town = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postcode = models.PositiveIntegerField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
    
    class Meta:
        db_table = "order_billing_details"
        verbose_name = "Order - Billing Details"
        verbose_name_plural = "Order - Billing Details"


class OrderCompanyTaxDetails(models.Model):
    order = models.ForeignKey(Order, related_name='order_company_tax_details', on_delete=models.CASCADE)
    VAT = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_activity = models.CharField(max_length=250)
    tax_location = models.CharField(max_length=100)
    
    phone = models.CharField(max_length=15, blank=True)

    address = models.CharField(max_length=255)
    address_number = models.PositiveIntegerField()
    town = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postcode = models.PositiveIntegerField()

    def __str__(self):
        return self.company_name
    
    class Meta:
        db_table = "order_company_tax_details"
        verbose_name = "Order - Company Tax Details"
        verbose_name_plural = "Order - Company Tax Details"
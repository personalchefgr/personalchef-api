# Generated by Django 4.1.3 on 2023-02-01 00:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CouponDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('is_percentage', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Coupon Discount',
                'verbose_name_plural': 'Coupon Discounts',
                'db_table': 'coupon_discounts',
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25)),
                ('is_active', models.BooleanField(default=False)),
                ('times_used', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coupons.coupondiscount')),
            ],
            options={
                'verbose_name': 'Coupon',
                'verbose_name_plural': 'Coupons',
                'db_table': 'coupons',
            },
        ),
    ]

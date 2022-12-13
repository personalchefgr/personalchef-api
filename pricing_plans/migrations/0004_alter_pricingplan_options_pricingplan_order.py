# Generated by Django 4.1.3 on 2022-12-13 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing_plans', '0003_remove_pricingplan_total_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pricingplan',
            options={'ordering': ['-price_per_meal'], 'verbose_name': 'Pricing Plan', 'verbose_name_plural': 'Pricing Plans'},
        ),
        migrations.AddField(
            model_name='pricingplan',
            name='order',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.3 on 2023-02-01 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dietary_plans', '0001_initial'),
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PricingPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=250)),
                ('price_per_meal', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('sort_order', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dietary_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dietary_plans.dietaryplan')),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptions.subscription')),
            ],
            options={
                'verbose_name': 'Pricing Plan',
                'verbose_name_plural': 'Pricing Plans',
                'db_table': 'pricing_plans',
                'ordering': ['sort_order'],
            },
        ),
    ]

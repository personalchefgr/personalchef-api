# Generated by Django 4.1.3 on 2023-01-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_order_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_code',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
    ]

# Generated by Django 4.1.3 on 2023-01-04 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_code',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-13 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-27 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dietary_plans', '0008_meal_img_alter_dietaryplan_meals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='meals'),
        ),
    ]

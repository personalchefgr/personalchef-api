# Generated by Django 4.1.3 on 2023-01-02 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dietary_plans', '0002_meal_snippet_meal_sort'),
    ]

    operations = [
        migrations.AddField(
            model_name='dietaryplan',
            name='snippet',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='dietaryplan',
            name='sort',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

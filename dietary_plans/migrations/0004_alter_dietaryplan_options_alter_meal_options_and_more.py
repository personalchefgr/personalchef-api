# Generated by Django 4.1.3 on 2023-01-02 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dietary_plans', '0003_dietaryplan_snippet_dietaryplan_sort'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dietaryplan',
            options={'ordering': ['sort_order'], 'verbose_name': 'Dietary Plan', 'verbose_name_plural': 'Dietary Plans'},
        ),
        migrations.AlterModelOptions(
            name='meal',
            options={'ordering': ['sort_order'], 'verbose_name': 'Meal', 'verbose_name_plural': 'Meals'},
        ),
        migrations.RenameField(
            model_name='dietaryplan',
            old_name='sort',
            new_name='sort_order',
        ),
        migrations.RenameField(
            model_name='meal',
            old_name='sort',
            new_name='sort_order',
        ),
    ]

from django.db import models
    
class MealOption(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "meal_options"
        verbose_name = "Meal Option"
        verbose_name_plural = "Meal Options"


class Subscription(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25)

    duration_choices = [
        ('week', 'Week'),
        ('month', 'Month')
    ]

    duration = models.CharField(
        max_length=25,  
        choices=duration_choices,
        default='week',   
    )

    meal_options = models.ManyToManyField(MealOption, blank=True)
    meals_per_day = models.IntegerField()

    number_of_weeks = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "subscriptions"
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"
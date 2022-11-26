from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=55)
    slug = models.SlugField(max_length=25)
    description = models.TextField(blank=True)

    calories = models.IntegerField(blank=True, null=True)
    protein = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    carbs = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    fat = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "meals"
        verbose_name = "Meal"
        verbose_name_plural = "Meals"


class DietaryPlan(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25)
    description = models.TextField(blank=True)

    meals = models.ManyToManyField(Meal, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "dietary_plans"
        verbose_name = "Dietary Plan"
        verbose_name_plural = "Dietary Plans"
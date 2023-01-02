from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=55)
    slug = models.SlugField(max_length=25)

    snippet = models.TextField(blank=True)
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to='meals', blank=True, null=True)

    sort_order = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "meals"
        ordering = ['sort_order']
        verbose_name = "Meal"
        verbose_name_plural = "Meals"


class MealNutrition(models.Model):
    meal = models.OneToOneField(Meal,primary_key=True, related_name='nutrition', on_delete=models.CASCADE)

    calories = models.IntegerField(blank=True, null=True)
    protein = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    carbs = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    fat = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal.name
    
    class Meta:
        db_table = "meal_nutrition_data"
        verbose_name = "Meal Nutrition"
        verbose_name_plural = "Meal Nutrition Data"



class DietaryPlan(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25)

    snippet = models.TextField(blank=True)
    description = models.TextField(blank=True)
    img = models.ImageField(
            upload_to='dietary_plans', 
            blank=True, 
            null=True)

    meals = models.ManyToManyField(Meal, 
            related_name='plans', 
            blank=True)

    sort_order = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "dietary_plans"
        ordering = ['sort_order']
        verbose_name = "Dietary Plan"
        verbose_name_plural = "Dietary Plans"
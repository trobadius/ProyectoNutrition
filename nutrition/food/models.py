from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo

    def get_absolute_url(self):
        return reverse('food:detail_category', args=[str(self.id)])

class TypeMeal(models.Model):
    meal_type = models.CharField(max_length=50)

    def __str__(self):
        return self.meal_type

    def get_absolute_url(self):
        return reverse('food:detail_type_meal', args=[str(self.id)])

class Food(models.Model):
    date = models.DateField()
    user_id = models.IntegerField()
    food_item = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    calories = models.IntegerField()
    protein = models.IntegerField()
    carbohydrates = models.IntegerField()
    fat = models.IntegerField()
    fiber = models.IntegerField()
    sugars = models.IntegerField()
    sodium = models.IntegerField()
    cholesterol = models.IntegerField()
    meal_type = models.ForeignKey(TypeMeal, on_delete=models.CASCADE)
    water_intake = models.IntegerField()

    def __str__(self):
        return self.date

    def get_absolute_url(self):
        return reverse('food:detail_food', args=[str(self.id)])
    
class ProfileUser(models.Model):
    ROLES = [
        ("user", "Usuario"),
        ("admin", "Administrador"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLES, default="user")

    def __str__(self):
        return f"{self.user.username} ({self.role})"
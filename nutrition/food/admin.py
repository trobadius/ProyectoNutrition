from django.contrib import admin
from .models import ProfileUser, Category, TypeMeal, Food
# Register your models here.

admin.site.register(ProfileUser)
admin.site.register(Category)
admin.site.register(TypeMeal)
admin.site.register(Food)
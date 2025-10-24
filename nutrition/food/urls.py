from django.urls import path
from .views import FoodListView, FoodDetailView, FoodCreateView, FoodUpdateView, FoodDeleteView, CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView, TypeMealListView, TypeMealDetailView, TypeMealCreateView, TypeMealUpdateView, TypeMealDeleteView, contacto_view
from django.shortcuts import render

app_name = 'food'

urlpatterns = [
    #Path Food
    path('', FoodListView.as_view(), name='lista_food'),
    path('food/<int:pk>/', FoodDetailView.as_view(), name='detail_food'),
    path('food/newfood/', FoodCreateView.as_view(), name='create_food'),
    path('food/<int:pk>/updatefood/', FoodUpdateView.as_view(), name='update_food'),
    path('food/<int:pk>/deletefood/', FoodDeleteView.as_view(), name='delete_food'),
    #Path Category
    path('category/', CategoryListView.as_view(), name='lista_category'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='detail_category'),
    path('category/newcategory/', CategoryCreateView.as_view(), name='create_category'),
    path('category/<int:pk>/updatecategory/', CategoryUpdateView.as_view(), name='update_category'),
    path('category/<int:pk>/deletecategory/', CategoryDeleteView.as_view(), name='delete_category'),
    #Path TypeMeal
    path('typemeal/', TypeMealListView.as_view(), name='lista_type_meal'),
    path('typemeal/<int:pk>/', TypeMealDetailView.as_view(), name='detail_type_meal'),
    path('typemeal/newtypemeal/', TypeMealCreateView.as_view(), name='create_type_meal'),
    path('typemeal/<int:pk>/updatetypemeal/', TypeMealUpdateView.as_view(), name='update_type_meal'),
    path('typemeal/<int:pk>/deletetypemeal/', TypeMealDeleteView.as_view(), name='delete_type_meal'),
    #Form
    path('form/', contacto_view, name='form'),
    path('gracias/', lambda r: render(r, 'food/gracias.html'), name='gracias'),
]
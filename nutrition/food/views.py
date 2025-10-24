from django.shortcuts import render
from .models import Food, Category, TypeMeal
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ContactoForm

# Create your views here.
#Food
class FoodListView(ListView):
    model = Food
    template_name = 'food/nutrition_food/lista_food.html'
    context_object_name = 'foods'

class FoodDetailView(DetailView):
    model = Food
    template_name = 'food/nutrition_food/detail_food.html'

class FoodCreateView(CreateView):
    model = Food
    template_name = 'food/nutrition_food/food_form.html'
    fields = ['date','user_id','food_item','category','calories','protein','carbohydrates','fat','fiber',
             'sugars','sodium','cholesterol','meal_type','water_intake']

class FoodUpdateView(UpdateView):
    model = Food
    template_name = 'food/nutrition_food/food_form.html'
    fields = ['date','user_id','food_item','category','calories','protein','carbohydrates','fat','fiber',
             'sugars','sodium','cholesterol','meal_type','water_intake']

class FoodDeleteView(DeleteView):
    model = Food
    template_name = 'food/nutrition_food/delete_food.html'
    success_url = reverse_lazy('food:lista_food')

#Category
class CategoryListView(ListView):
    model = Category
    template_name = 'food/category/lista_category.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'food/category/detail_category.html'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'food/category/category_form.html'
    fields = ['tipo']

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'food/category/category_form.html'
    fields = ['tipo']

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'food/category/delete_category.html'
    success_url = reverse_lazy('food:lista_category')

#TypeMeal
class TypeMealListView(ListView):
    model = TypeMeal
    template_name = 'food/type_meal/lista_type_meal.html'
    context_object_name = 'typemeals'

class TypeMealDetailView(DetailView):
    model = TypeMeal
    template_name = 'food/type_meal/detail_type_meal.html'

class TypeMealCreateView(CreateView):
    model = TypeMeal
    template_name = 'food/type_meal/type_meal_form.html'
    fields = ['meal_type']

class TypeMealUpdateView(UpdateView):
    model = TypeMeal
    template_name = 'food/type_meal/type_meal_form.html'
    fields = ['meal_type']

class TypeMealDeleteView(DeleteView):
    model = TypeMeal
    template_name = 'food/type_meal/delete_type_meal.html'
    success_url = reverse_lazy('food:lista_type_meal')

#Forms
def contacto_view(request):
    form = ContactoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        nombre = form.cleaned_data['nombre']
        email = form.cleaned_data['email']
        telefono = form.cleaned_data['telefono']
        return render(request, 'food/gracias.html', {'nombre': nombre})
    return render(request, 'food/formulario.html', {
        'form': form,
        'titulo': 'Formulario',
    })

def gracias_view(request):
    return render(request, 'food/gracias.html')
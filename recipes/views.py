from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
from recipes.views import contato, home
# Create your views here.

def home(request):
    recipes = Recipe.objects.all()
    return HttpResponse(f"Number of recipes: {recipes.count()}")
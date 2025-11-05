from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
from recipes.views import contato, home
# Create your views here.


#teste
def home(request):
    HttpResponse("home")
    
def contato(request):
    HttpResponse("contato")

def sobre(request):
    HttpResponse("sobre")        
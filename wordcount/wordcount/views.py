from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  return render(request, 'home.html')

def teste(request):
  return HttpResponse("<h1>teste de url</h1>")

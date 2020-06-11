from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def generate(request):
    return render(request, 'generator/generate.html')

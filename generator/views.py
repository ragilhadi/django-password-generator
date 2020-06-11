from django.shortcuts import render
import random
import string
# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def generate(request):
    passgenerate = ''
    # list lowercase
    lowerCase = string.ascii_lowercase
    charachter = list(lowerCase)
    # list uppercase
    if request.GET.get('uppercase'):
        upperCase = string.ascii_uppercase
        charachter.extend(list(upperCase))

    if request.GET.get('number'):
        number = list('1234567890')
        charachter.extend(list(number))

    if request.GET.get('special'):
        special = list('!&*#?+~')
        charachter.extend(list(special))

    length = int(request.GET.get('length'))

    for x in range(length):
        passgenerate += random.choice(charachter)

    return render(request, 'generator/generate.html', {'password': passgenerate})

from django.shortcuts import render
import random

# Create your views here.

def index(request):
    context = {
        'random_int': random.randint(1,1000000),
    }
    return render(request, 'random_generator/index.html', context)
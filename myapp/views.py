from django.shortcuts import render, get_object_or_404, reverse
from .models import Product
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotFound
import json
from .forms import ProductForm

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'myapp/index.html', {'products':products})

def detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'myapp/detail.html', {'product': product})

def create_product(request):
    product_form = ProductForm()
    return render(request, 'myapp/create_product.html', {'product_form':product_form})
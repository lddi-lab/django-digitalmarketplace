from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Product
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotFound
import json
from .forms import ProductForm, UserRegistrationForm

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'myapp/index.html', {'products':products})

def detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'myapp/detail.html', {'product': product})

def create_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            new_product = product_form.save(commit=False)
            new_product.seller = request.user
            new_product.save()
            return redirect('index')

    product_form = ProductForm()
    return render(request, 'myapp/create_product.html', {'product_form':product_form})

def product_edit(request, id):
    product = Product.objects.get(id=id)
    product_form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if request.method == 'POST':
        if product_form.is_valid():
            product_form.save()
        return redirect('index')
    return render(request, 'myapp/product_edit.html', {'product_form':product_form, 'product': product})

def product_delete(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('index')
    return render(request, 'myapp/delete.html', {'product':product})

def dashboard(request):
    products = Product.objects.all()
    return render(request, 'myapp/dashboard.html', {'products':products })


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        new_user = user_form.save(commit=False)
        new_user.set_password(user_form.cleaned_data['password'])
        new_user.save()
        return redirect('index')
    user_form = UserRegistrationForm()
    return render(request, 'myapp/register.html', {'user_form':user_form})
from difflib import context_diff
from multiprocessing import context
from django.shortcuts import render
from product.models import Product
from category.models import Category
from account.views import LoginView

def index(request):
    category = Category.objects.all()
    product = Product.objects.all()
    context = {'product':product, 'category': category }
    return render(request, 'main/index.html', context = context)

def product_detail(request, id):
    product = Product.objects.get(pk=id)
    context = {'product':product}
    return render(request, 'main/products.html', context=context)

def login_user(request, id):
    login = LoginView.objects.all()
    context = {'login': login}
    return render(request, 'main/Login.html', context=context)
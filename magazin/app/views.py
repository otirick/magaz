from django.shortcuts import render, redirect
from .models import *


def index(request):

    if request.method == 'POST':
        print('post')
        return render(request, 'index.html')

    cats = ['T-Shirts', '123', '321', '1', '123123']
    return render(request, 'index.html', {'cats': cats})


def cart(request):
    return render(request, 'cart.html')


def product_add(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price') + ' RUB'
        Product.objects.create(name=name, price=price)
        return render(request, 'product_add.html', {'message': f'Успешно создан товар {name}'})

    return render(request, 'product_add.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_page(request, id):
    product = Product.objects.get(id=id)
    price = product.get_dollar_price()
    return render(request, 'product.html', {'product': product, 'price': price})

# TODO: подключаем админку 123

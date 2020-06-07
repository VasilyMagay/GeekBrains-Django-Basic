from django.shortcuts import render, get_object_or_404
import json
from mainapp.models import ProductCategory, Product
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_basket(user):
    if user.is_authenticated:
        return user.basket_set.all().order_by('product__category')
    return []


def index(request):

    basket = get_basket(request.user)

    context = {
        'page_title': '',
        'basket': basket,
    }
    return render(request, 'mainapp/index.html', context)


def products(request, category_pk=None, page=1):

    basket = get_basket(request.user)

    categories = ProductCategory.objects.filter(is_active=True)
    products = Product.objects.filter(is_active=True)

    if category_pk:
        if category_pk != '0':
            products = Product.objects.filter(category_id=category_pk, is_active=True)

        products_paginator = Paginator(products, 2)

        try:
            products = products_paginator.get_page(page)
        except PageNotAnInteger:
            products = products_paginator.get_page(1)
        except EmptyPage:
            products = products_paginator.get_page(products_paginator.num_pages)

        context = {
            'page_title': ' | каталог',
            'products': products,
            'categories': categories,
            'basket': basket,
            'category_pk': category_pk,
        }
        return render(request, 'mainapp/products_list.html', context)
    else:
        hot_product = random.choice(products)
        same_products = Product.objects.filter(category=hot_product.category, is_active=True).exclude(pk=hot_product.pk)
        context = {
            'page_title': ' | каталог',
            'categories': categories,
            'basket': basket,
            'hot_product': hot_product,
            'same_products': same_products,
        }
        return render(request, 'mainapp/products.html', context)


def product(request, pk):

    categories = ProductCategory.objects.filter(is_active=True)
    basket = get_basket(request.user)

    context = {
        'title': 'продукт',
        'categories': categories,
        'product': get_object_or_404(Product, pk=pk),
        'basket': basket,
    }

    return render(request, 'mainapp/product.html', context)


def contact(request):

    basket = get_basket(request.user)

    # locations = [
    #     {
    #         'city': 'Москва',
    #         'phone': '+7-495-100-10-10',
    #         'email': 'moscow@catalog.ru',
    #         'address': 'В пределах МКАД',
    #     },
    #     {
    #         'city': 'Санкт-Петербург',
    #         'phone': '+7-812-200-20-20',
    #         'email': 'spb@catalog.ru',
    #         'address': 'В пределах КАД',
    #     },
    #     {
    #         'city': 'Псков',
    #         'phone': '+7-987-300-30-30',
    #         'email': 'pskov@catalog.ru',
    #         'address': 'У стен кремля',
    #     }
    # ]
    #
    # with open('json/locations.json', 'w', encoding='utf-8') as tmp_file:
    #     json.dump(locations, tmp_file)

    with open('json/locations.json', 'r', encoding='utf-8') as tmp_file:
        locations = json.load(tmp_file)

    context = {
        'page_title': ' | контакты',
        'locations': locations,
        'basket': basket,
    }

    return render(request, 'mainapp/contact.html', context)


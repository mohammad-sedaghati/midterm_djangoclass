from django.shortcuts import render
from .models import Products
# Create your views here.


def product_category(request, cat):
    return render(request, 'product_list_page.html', {
        'products': Products.objects.filter(category=cat)
    })


def product_tags(request, tag):
    return render(request, 'product_list_page.html', {
        'products': Products.objects.filter(tag=tag)
    })


def product_detail(request, slug):
    return render(request, 'product_detail.html', {
        'product': Products.objects.filter(slug=slug).first()
    })

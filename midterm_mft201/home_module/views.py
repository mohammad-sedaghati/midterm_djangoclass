from django.shortcuts import render
from product_module.models import Products

# Create your views here.

def home_page(request):
    return render(request, 'home_page.html', {
        # 'slides': slides,
        # 'products': products
    })

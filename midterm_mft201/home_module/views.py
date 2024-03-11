from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, '_layout.html', {
        # 'slides': slides,
        # 'products': products
    })

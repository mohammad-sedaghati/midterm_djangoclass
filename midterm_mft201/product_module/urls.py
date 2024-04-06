from django.urls import path
from . import views

urlpatterns = [
    path('<cat>/', views.product_category, name='product_cat'),
    path('<tag>/', views.product_tags, name='product_tag'),
    path('<slug>/', views.product_detail, name='product_detail')
]

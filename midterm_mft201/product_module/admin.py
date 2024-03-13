from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(ProductTags)
admin.site.register(ProductCategory)
admin.site.register(ProductCategoryPart)
admin.site.register(ProductCategoryAccurate)
admin.site.register(Products)

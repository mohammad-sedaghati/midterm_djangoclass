from django.apps import AppConfig

# Register your models here.


class ProductModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product_module'
    verbose_name = 'محصولات'

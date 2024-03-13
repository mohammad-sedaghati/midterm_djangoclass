from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='نام دسته بندی')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی های محصول'


class ProductCategoryPart(models.Model):
    title = models.CharField(max_length=100, verbose_name='نام دسته بندی')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='دسته بندی')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی های محصول'


class ProductCategoryAccurate(models.Model):
    title = models.CharField(max_length=100, verbose_name='نام دسته بندی')
    address_category = models.CharField(max_length=100, verbose_name='آدرس در مرورگر')
    category = models.ForeignKey(ProductCategoryPart, on_delete=models.CASCADE, verbose_name='دسته بندی')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی های محصول'


class ProductTags(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان تگ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'


class Products(models.Model):
    title = models.CharField(max_length=100, verbose_name='نام کالا')
    slug = models.SlugField(verbose_name='آدرس در مرورگر')
    price = models.IntegerField(verbose_name='قیمت')
    off = models.IntegerField(verbose_name='تخفیف')
    short_detail = models.CharField(max_length=100, verbose_name='توضیحات کوتاه')
    long_detail = models.TextField(verbose_name='توضیحات بلند')
    category = models.ForeignKey(ProductCategoryAccurate, on_delete=models.CASCADE, verbose_name='دسته بندی')
    tag = models.ManyToManyField(ProductTags, verbose_name='تگ')
    is_active = models.BooleanField(verbose_name='موجود', default=True)
    is_delete = models.BooleanField(verbose_name='حذف شده', default=False)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

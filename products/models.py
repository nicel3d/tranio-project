from django.db import models

# Create your models here.
class ShopStatus(models.Model):
    name = models.CharField(max_length=23, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        managed = False
        db_table = 'shop_status'
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'

class ShopProducts(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    ordering = models.IntegerField(blank=True, null=True)
    status = models.ForeignKey(ShopStatus, on_delete=None, default=1)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products_img')
    id_category = models.ForeignKey('categories.ShopCategories', models.DO_NOTHING, db_column='id_category', blank=True, null=True)
    alias = models.CharField(max_length=40, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Продукт: %s, %s" % (self.title, self.status.name)

    class Meta:
        managed = False
        db_table = 'shop_products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ShopProductsImage(models.Model):
    product = models.ForeignKey('ShopProducts', blank=True, null=True, default=None, on_delete=None)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products_img')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Продукт: %s" % self.id

    class Meta:
        managed = False
        db_table = 'shop_products_image'
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
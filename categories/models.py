from django.db import models

# Create your models here.
class ShopCategories(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    ordering = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='categories_img')
    alias = models.CharField(max_length=40, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    url = ''

    def __str__(self):
        return '%s' % self.title

    class Meta:
        managed = False
        db_table = 'shop_categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

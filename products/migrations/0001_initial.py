# Generated by Django 2.0 on 2017-12-29 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=40, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('ordering', models.IntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('alias', models.CharField(blank=True, max_length=40, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'db_table': 'shop_products',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ShopProductsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='product_image')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотографии',
                'db_table': 'shop_products_image',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ShopStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=23, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Статус заказа',
                'verbose_name_plural': 'Статусы заказа',
                'db_table': 'shop_status',
                'managed': False,
            },
        ),
    ]
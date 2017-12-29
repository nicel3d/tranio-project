from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from products.models import ShopProducts


def product(request):
    title = 'Category'
    return render(request, 'products/product.html', locals())

def products(request):
    products_list = ShopProducts.objects.all()
    paginator = Paginator(products_list, 25) # Show 25 contacts per page
    title = 'Продукты'
    count_products = len(products_list)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'products/list.html', locals()) #{'products': products}
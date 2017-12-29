import numpy as np
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from products.models import ShopProducts
from categories.models import ShopCategories

def category(request):
    title = 'Category'
    return render(request, 'categories/category.html', locals())

def home(request, page = None):
    cat_all = ShopCategories.objects.all().order_by('ordering')
    cat = None
    if page == None:
        cat = ShopCategories.objects.first()
    else:
        cat_id = str(page).split('/')
        cat_id = list(filter(None, cat_id))
        lvl_urls = lvlUrls(cat_all, cat_id)
        if len(cat_id) == len(lvl_urls):
           cat = ShopCategories.objects.get(alias=cat_id[-1], id=lvl_urls[-1])
        else:
            raise Http404("Article does not exist on this site")
    #rr = np.concatenate(cat).astype(None)

    breadcrumbs = []
    items = lvlTree(cat_all, cat.parent_id)
    items = list(reversed(items[0]))
    for i, item in enumerate(items):
        index = 0
        alias = []
        while i >= index:
            alias.append(items[index])
            index += 1
        title = cat_all.filter(alias=item)
        breadcrumbs.append(['/'.join(alias), title[0]])

    catalog = buildTree(cat_all)
    sorting = parentCatId(cat_all, cat.id)

    if len(sorting) > 0:
        products_list = ShopProducts.objects.all().filter(id_category__in=sorting).order_by('ordering')
    else:
        products_list = ShopProducts.objects.all().filter(id_category=int(cat.id)).order_by('ordering')

    i = 0
    paginator = Paginator(products_list, 12) # Show 25 contacts per page
    title = 'Электронный каталог'
    count_products = len(products_list)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'categories/home.html', locals())

def parentCatId(elements, id):
    parent_id = [id]
    select_id = [id]
    not_arr = []
    while len(select_id) > 0:
        select_id = []
        for index, element in enumerate(elements):
            if element.parent_id in parent_id and index not in not_arr:
                select_id.append(element.id)
                parent_id.append(element.id)
                not_arr.append(index)
    return list(reversed(parent_id))

def buildTree(elements, parentId = 0):
        branch = []
        for element in elements:
            if element.parent_id == parentId:
                prefix = lvlTree(elements, element.id)
                name = ""
                i = 1
                while i <= int(prefix[1]):
                    name += '&nbsp;&nbsp;'
                    i = i + 1
                element.url = '/'.join(list(reversed(prefix[0])))
                branch.append(element)
                branch[-1].title = name + element.title
                branch += buildTree(elements, element.id)
        return branch

def lvlTree(elements, id = 0):
    level = 0
    alias = []
    while id != 0:
        index = None
        for i, element in enumerate(elements):
            if element.id == id:
                index = i
                break
        id = 0
        if index != None:
            id = elements[index].parent_id
            alias.append(elements[index].alias)
            if id != 0:
                level = level + 1
    return [alias, level]

def lvlUrls(elements, list_url):
    arr = []
    parent_id = None
    i = 0
    while len(list_url) > i:
        vh = None
        for element in elements:
            if parent_id == None:
                if str(element.alias) == str(list_url[i]):
                    parent_id = element.id
                    vh = 1
                    break
            else:
                if str(element.alias) == str(list_url[i]) and element.parent_id == parent_id:
                    parent_id = element.id
                    vh = 1
                    break
        i = i + 1
        if parent_id != None and vh == 1:
            arr.append(parent_id)
        else:
            break
    return arr
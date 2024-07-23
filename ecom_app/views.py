from django.shortcuts import render
from .models import Products, SubCategory, Category
import ast
# Create your views here.
def home(request):
    category_furniture = SubCategory.objects.filter(category__name="furniture")
    category_interior = SubCategory.objects.filter(category__name="interior")
    return render(request, 'home.html', {'category_furniture': category_furniture, 'category_interior': category_interior})
def about(request):
    return render(request, 'about.html')
def furniture(request):
    category_products = SubCategory.objects.filter(category__name="furniture")
    return render(request, 'category.html', {'category_products': category_products, 'title' : 'FURNITURE CATEGORIES'})
def interior(request):
    category_products = SubCategory.objects.filter(category__name="interior")
    return render(request, 'category.html', {'category_products': category_products, 'title': 'INTERIOR CATEGORIES'})
def enquiry(request):
    return render(request, 'enquiry.html')
def contact(request):
    return render(request, 'contact.html')
def bathroom(request):
    return render(request, 'interiors/bathroom.html')

def product(request,cat_id):
    products = Products.objects.all()

    return render(request, 'products_list/products_list.html', {'cat_id': cat_id, 'products': products})

def detail(request,cat_id,single_id):

    products = Products.objects.filter(id_num=single_id)
    specifications = {}
    #logic for specification
    for product in products:
        spec_dict = eval(product.specification)
        specifications.update(spec_dict)

    return render(request, 'single_product_detail/single_product_detail.html', {'cat_id': cat_id, 'single_id': single_id,'products':products, 'specifications':specifications})


from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.catagory import Category

def index(request):
    products=None
    categories=Category.get_category()
    categoryId=request.GET.get('category')
    if categoryId:
        products = Product.get_all_product_data_by_category_id(categoryId)
    else:
        products = Product.get_all_product_data()
    data={}
    data['products']=products
    data['categories']=categories
    return render(request,'index.html',data)


def signup(request):
    return render(request,'signup.html')
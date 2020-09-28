from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.catagory import Category
from .models.customer import Customer

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
    if request.method=='POST':
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        phone=request.POST['phone']
        email=request.POST['email']
        password=request.POST['password']


        error_message=None
        if not firstname:
            error_message="Fill the first name"
        elif len(firstname)<5:
            error_message="Firstname must be longer than 4 character"
        elif not lastname:
            error_message="Fill the last name"
        elif len(password)<6:
            error_message="Password lenght must be atleast 7"


        if not error_message:
            customerlist=Customer( firstname=firstname,lastname=lastname ,phone= phone ,email=email, password=password )
            customerlist.save()
            return render(request,'index.html')
        else:    
            values={
            'error': error_message,
            'firstname':firstname,
            'lastname': lastname,
            'phone': phone,
            'email': email,
            }
            return render(request,'signup.html',values)
    else:
        return render(request,'signup.html')
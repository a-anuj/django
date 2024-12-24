from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def products(request):
    all_products = Product.objects.all()
    context = {
        'products':all_products
    }
    return render(request,'myapp/index.html',context)

def product_details(request,id):
    product = Product.objects.get(id=id)
    context = {
        'product':product
    }
    return render(request,'myapp/details.html',context)

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']
        product = Product(name=name,price=price,desc=desc,image=image)
        product.save()
    return render(request,'myapp/addproduct.html')
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def products(request):
    all_products = Product.objects.all()
    context = {
        'products':all_products
    }
    return render(request,'myapp/index.html',context)


class ProductListView(ListView):
    model = Product
    template_name = 'myapp/index.html'
    context_object_name = 'products'


def product_details(request,id):
    product = Product.objects.get(id=id)
    context = {
        'product':product
    }
    return render(request,'myapp/details.html',context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'myapp/details.html'
    context_object_name = 'product'


@login_required
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']
        seller_name = request.user
        product = Product(name=name,price=price,desc=desc,image=image,seller_name=seller_name)
        product.save()
    return render(request,'myapp/addproduct.html')


class ProductCreateView(CreateView):
    model = Product
    fields = ['name','price','desc','image','seller_name']

    


def update_product(request,id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.desc = request.POST.get('desc')
        product.image = request.FILES['upload']
        product.save()
        return redirect('/myapp/products')
    context = {
        "product" : product,
    }
    return render(request,'myapp/updateproduct.html',context)

def delete_product(request,id):
    product = Product.objects.get(id=id)
    context = {
        'product' : product,
    }
    if request.method == 'POST':
        product.delete()
        return redirect('/myapp/products')
    return render(request,'myapp/delete.html',context)

def my_listings(request):
    products = Product.objects.filter(seller_name=request.user)
    context = {
        'products' : products
    }

    return render(request,'myapp/mylistings.html',context)
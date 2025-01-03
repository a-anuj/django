from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def products(request):
    page_obj = all_products = Product.objects.all()

    product_name = request.GET.get('product_name')
    if product_name!='' and product_name is not None:
        page_obj = all_products.filter(name__icontains=product_name)

    paginator = Paginator(page_obj,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':page_obj
    }
    return render(request,'myapp/index.html',context)


class ProductListView(ListView):
    model = Product
    template_name = 'myapp/index.html'
    context_object_name = 'products'
    paginate_by = 3


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


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name','price','desc','image','seller_name']
    template_name_suffix = '_update_form'


def delete_product(request,id):
    product = Product.objects.get(id=id)
    context = {
        'product' : product,
    }
    if request.method == 'POST':
        product.delete()
        return redirect('/myapp/products')
    return render(request,'myapp/delete.html',context)


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('myapp:products')

def my_listings(request):
    products = Product.objects.filter(seller_name=request.user)
    context = {
        'products' : products
    }

    return render(request,'myapp/mylistings.html',context)
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def products(request):
    all_products = Product.objects.all()
    return HttpResponse(all_products) 
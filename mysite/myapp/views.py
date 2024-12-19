from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def products(request):
    all_products = ["Apple","Mango","Banana","Cherry","Kiwi","Jack Fruit"]
    return HttpResponse(products)
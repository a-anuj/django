from django.contrib import admin
from .models import Product
# Register your models here.

admin.site.register(Product)
admin.site.site_header = "Buy and Sell Website"
admin.site.site_title = "QuickCart"
admin.site.index_title = "Manage QuickCart"
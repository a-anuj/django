from django.contrib import admin
from .models import Product
# Register your models here.


admin.site.site_header = "Buy and Sell Website"
admin.site.site_title = "QuickCart"
admin.site.index_title = "Manage QuickCart"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','desc')
    search_fields = ('name',)

    def setPricetoZero(self,request,queryset):
        queryset.update(price=0)
    
    actions = ('setPricetoZero',)
    list_editable = ('price','desc')

admin.site.register(Product,ProductAdmin)
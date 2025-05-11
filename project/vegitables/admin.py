from django.contrib import admin
from vegitables.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','cat']
    list_filter=['cat','is_active','price']

admin.site.register(Product,ProductAdmin)
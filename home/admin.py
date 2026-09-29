from django.contrib import admin
from .models import Category, Product
admin.site.register(Category)
class categoryadmin(admin.ModelAdmin):
    list_display = ('slug' , 'name' )
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available', 'created']
    list_filter = ['available', 'category']
    prepopulated_fields = {'slug': ('name',)}



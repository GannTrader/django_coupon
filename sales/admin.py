from django.contrib import admin
from .models import Product, Discount, Cart


class ProductAdmin(admin.ModelAdmin):
	list_display = ['title', 'created_at']
	list_filter = ['created_at']
	search_fields = ['title', 'description']

class Discountdmin(admin.ModelAdmin):
	list_display = ['code', 'name', 'created_at', 'expire', 'percent']
	list_filter = ['created_at', 'expire']

class CartAdmin(admin.ModelAdmin):
	list_display = ['user', 'product', 'quantity', 'price', 'created_at']


admin.site.register(Product, ProductAdmin)
admin.site.register(Discount, Discountdmin)
admin.site.register(Cart, CartAdmin)
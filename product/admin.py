from django.contrib import admin
from product.models import Cart, Product, Order, Wishlist

class display_product(admin.ModelAdmin):
    list_display = ('title', 'image', 'price', 'brand', 'stock')

class display_Cart(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'price', 'date')

admin.site.register(Product, display_product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Wishlist)
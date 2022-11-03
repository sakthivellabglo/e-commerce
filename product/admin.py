from django.contrib import admin
from product.models import Brand, Cart, Product, Order, Wishlist


class display_product(admin.ModelAdmin):
    list_display = ('title', 'image', 'price', 'brand', 'stock')
    search_fields = ['brand__name','title']
    list_display_links = ('title','brand')
    list_editable = ('price','stock')
    sortable_field_name = "title"
    list_filter =  ('title','brand')


class display_Cart(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'price', 'date')


admin.site.register(Product, display_product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Wishlist)
admin.site.register(Brand)
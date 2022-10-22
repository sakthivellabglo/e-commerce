from django.contrib import admin

from product.models import Cart, Product

class display_product(admin.ModelAdmin):
	list_display = ('title','image', 'price', 'brand','stock')

admin.site.register(Product, display_product)
admin.site.register(Cart)


# Register your models here.

from django.http import HttpResponse
from django.views.generic.list import ListView
from django.db.models import Q
from django .contrib import messages
from product.models import Cart, Order, Product, Wishlist
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from django.db.models import Sum, F


class Allproducts(ListView):
    model = Product
    template_name = "allproducts.html"


class Searchresult(ListView):
    model = Product
    template_name = "product.html"

    def get_queryset(self):
        query1 = self.request.GET.get("product_name")
        object_list = Product.objects.filter(
            (Q(title__icontains=query1) | Q(brand__icontains=query1)) & ~Q(stock__contains="0"))
        if object_list.exists():
            pass
        else:
            messages.error(self.request, 'Products Are Not Found')
        return object_list


@login_required
def Add_to_add(request, id):
    product = Product.objects.get(id=id)
    cart, create = Cart.objects.get_or_create(
        product=product,
        user=request.user,
        price=product.price,
        is_active=True)
    return redirect("all")


@login_required
def cart_remove(request, id):
    remove_item = Cart.objects.get(id=id)
    remove_item.delete()
    return redirect("cart")

@login_required
def order_remove(request, id):
    remove_item = Cart.objects.get(id=id)
    remove_item.delete()
    return redirect("order")

@login_required
def add_quntity(request, id):
    product = Product.objects.get(id=id)
    cart = Cart.objects.filter(product=product)
    qunt = request.GET.get('quantity')
    cart.update(quantity=qunt)
    return redirect("cart")


@login_required
def add_order(request):
    cart = Cart.objects.filter(user=request.user)
    total = Cart.objects.filter(Q(user=request.user) & Q(is_active=False)).aggregate(
        price__sum=Sum(F('price') * F('quantity')))['price__sum']
    cart.update(is_active=False)
    orders = Order.objects.create(user_id=request.user.id)
    order =  Order.objects.get(id=orders.id)
    order.total_product_cost = int(total)
    order.tax = 18
    order.save()
    order.items.add(*cart)
    return redirect("order")


class Orderproducts(ListView):
    model = Order
    template_name = "order.html"

    def get_queryset(self):
        object_list = Order.objects.filter(user=self.request.user)
        if object_list.exists():
            pass
        else:
            messages.error(self.request, ' nothing to order  ')
        return object_list

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['sub_total'] = Order.objects.filter(user=self.request.user).aggregate(
            total_product_cost__sum=Sum(('total_product_cost')))['total_product_cost__sum']
        context['tax'] =Cart.objects.filter(user=self.request.user).aggregate(
            total=Sum(F('price') *18/100))['total']
        if context['sub_total'] is not None:
            context['total_price'] = context['sub_total'] + context['tax']
        return context


class ListCartItem(ListView):
    model = Cart
    context_object_name = 'cartitems'
    template_name = 'list_cartitems.html'

    def get_queryset(self):
        object_list = Cart.objects.filter(
            (Q(user=self.request.user) & Q(is_active=True)))
        if object_list.exists():
            pass
        else:
            messages.error(self.request, ' your cart is empty  ')
        return object_list

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['total_price'] = self.get_queryset().aggregate(Sum('price'))[
            'price__sum']
        return context


@login_required
def order_place(request):
    return HttpResponse("your order is placed")

def wishlist(request,id):
    wish_product = Product.objects.get(id = id)
    obj,add_wish = Wishlist.objects.get_or_create(user = request.user,product = wish_product)
    return redirect('all')

def rm_wishlist(request,id):
    wish_product = Product.objects.get(id = id)
    wish_product.delete()
    return redirect('wish')

class Wishproducts(ListView):
    model = Wishlist
    template_name = "wish.html"



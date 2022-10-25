from django.http import HttpResponse
from django.views.generic.list import ListView
from django.db.models import Q
from django .contrib import messages
from product.models import Cart, Order, Product
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models import Sum , F

class Allproducts(ListView):
     model = Product
     template_name = "allproducts.html"

class Searchresult(ListView):
    model = Product
    template_name = "product.html"

    def get_queryset(self): 
        query1 =self.request.GET.get("product_name")
        object_list =Product.objects.filter(
            (Q(title__icontains=query1) | Q(brand__icontains=query1)) & ~Q(stock__contains= "0")
            )
        if object_list.exists() :
            pass
        else:
           messages.error(self.request, 'Products Are Not Found')
        return object_list


@login_required
def Add_to_add(request,id):
    product = Product.objects.get(id=id)
    cart = Cart.objects.get_or_create(
         product= product,
        user = request.user,
        price = product.price ,
    )
    return redirect("all")

@login_required
def cart_remove(request, id):
    remove_item= Cart.objects.get(id=id)
    remove_item.delete()
    return redirect("cart")

def add_quntity(request,id):
    product = Product.objects.get(id=id)
    cart = Cart.objects.get(product =  product)
    qunt = request.GET.get('quantity')
    cart.quantity = qunt
    cart.price =  product.price * int(qunt)
    cart.save()
    return redirect("cart")

def add_order(request,id):
    cart =  Cart.objects.get(id=id)
    order = Order.objects.get_or_create(
        items= cart,
        user = request.user,
        total_product_cost = cart.price ,
        tax =12,
    )
    return redirect("order")
class Orderproducts(ListView):
     model = Order
     template_name = "order.html"
     
     def get_queryset(self): 
        object_list =Order.objects.filter(user = self.request.user)
        if object_list.exists() :
            pass
        else:
           messages.error(self.request, ' nothing to order  ')
        print(object_list)
        return object_list
    
     def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['sub_total'] = Order.objects.filter(user = self.request.user).aggregate(Sum('total_product_cost'))['total_product_cost__sum']
        context['tax'] = Order.objects.filter(user = self.request.user).aggregate(total = Sum(F('total_product_cost')* F('tax')/100))['total'] 
        context['total_price'] = context['sub_total'] + context['tax']
        return context


 
class ListCartItem(ListView):
    model = Cart
    context_object_name = 'cartitems'
    template_name='list_cartitems.html'
    '''override the get_queryset method '''
    def get_queryset(self): 
        object_list =Cart.objects.filter(user = self.request.user)
        if object_list.exists() :
            pass
        else:
           messages.error(self.request, ' your cart is empty  ')
        return object_list
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        '''Add context to total price'''
        context['total_price'] = self.get_queryset().aggregate(Sum('price'))['price__sum'] 
        return context
def order_place(request):
    return HttpResponse("your order is placed")
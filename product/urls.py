from django.urls import path ,include
from django.contrib.auth.decorators import login_required

from product import views
urlpatterns = [ path('all/',views.Allproducts.as_view(),name='all'),
                path('search/',views.Searchresult.as_view(),name='search_results'),
                path("accounts/", include("django.contrib.auth.urls")),
                path("cart/",login_required(views.ListCartItem.as_view()),name='cart'),
                path("add_to_card/<int:id>",views.Add_to_add,name="add_to_cart"),
                path("add_quntity/<int:id>",views.add_quntity,name="add_quntity"),
                path('remove/<int:id>/', views.cart_remove, name='cart_remove'),
                path("add_to_order",views.add_order,name="add_to_order"),
                path("order",views.Orderproducts.as_view(),name='order'),
                path("placeorder",views.order_place,name = 'order_place'), 
        
]
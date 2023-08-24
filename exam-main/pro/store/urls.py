from django.urls import path
from . import views


urlpatterns = [
    path('product_detail/<int:product_id>/',views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/',views.add_to_cart, name='add_to_cart'),
    path('cart/',views.cart_view, name='cart_view'),
    path('change-quantity/<str:product_id>',views.change_quantity, name='change_quantity'),
    path('remove-from-cart/<str:product_id>/',views.remove_from_cart,name='remove_from_cart'),
]

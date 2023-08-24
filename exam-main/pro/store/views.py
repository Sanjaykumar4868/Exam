from django.shortcuts import render,get_object_or_404,redirect
from store.models import Product
from .cart import Cart
# Create your views here.


def productpage(request):
    products = Product.objects.all()

    return render(request,'product.html',{
        'products':products
    })


def product_detail(request, product_id):
   
    product = get_object_or_404(Product, id = product_id )

    return render(request, 'product_detail.html',{
        'product':product
    })
                  


def cart_view(request):
    cart = Cart(request)

    return render(request, 'cart_view.html',{
        'cart': cart
    })

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return redirect('productpage')



def change_quantity(request,product_id):
    action = request.GET.get('action', '')

    if action:
        quantity = 1

        if action == 'decrease':
            quantity = -1
        cart = Cart(request)
        cart.add(product_id,quantity, True)

    return redirect('cart_view')


def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)

    return redirect('cart_view')
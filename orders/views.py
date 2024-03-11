from django.shortcuts import render, redirect

# Create your views here.

from orders.models import Order
from cart.models import CartItem, Cart

def get_orders(request):
    curr_user_profile = request.user.profile
    user_orders = Order.objects.filter(user=curr_user_profile)

    context={
        "user_orders":user_orders
    }
    return render(request, "accounts/orders.html", context)


def confirm_order(request):
    if request.method == "POST":
        curr_user_profile = request.user.profile

        """
        Add paypal payments
        Add correct status 
        
        """
        cart_items = CartItem.objects.filter(user=request.user)
        cart = Cart.objects.get(user=request.user)
        if not cart_items:
            return redirect('/')
        
        new_order = Order.objects.create(user=curr_user_profile,status=1,payment=2)

        new_order.sum = sum(item.quantity * item.product.price for item in cart.items.all())
        
        new_order.save()

        for cart_item in cart_items:
            new_order.items.add(cart_item)
        cart_items.delete()

        ## clear() on Cart object(attr items), clearing related items, but not deleting them - makes mess
        ## delete() in this way, deleting rows from db 


        return redirect('/')
    else:
        return redirect('/')
    
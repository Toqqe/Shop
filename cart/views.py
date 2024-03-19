from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

import json

from cart.models import Cart, CartItem
from shop.models import Product
from coupons.models import Coupon
from accounts.models import Address

from accounts.forms import DeliveryAddressForm
# Create your views here.


def cart_modal(request):
    cart_obj, created  = Cart.objects.get_or_create(user=request.user)
    modal_template_name = "cart/includes/cart_modal_items.html"
    total_price = sum(item.quantity * item.product.price for item in cart_obj.items.all())

    context = {
        "cart":cart_obj,
        "total_price": total_price
    }

    return render(request, modal_template_name, context)

@require_http_methods(["POST"])
def add_to_cart(request):
    if request.method == "POST":

        data = json.loads(request.body)
        prod_id = data.get('productId')
        curr_user = request.user
        product = get_object_or_404(Product, pk=prod_id)
        
        if curr_user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=curr_user)
            cart_item, item_created = CartItem.objects.get_or_create(user=curr_user, product=product)
            cart.items.add(cart_item) ## Add exception if quanitity > 10 return error (10 max value of items) 

            if not item_created:
                if not (cart_item.quantity == 10):
                    cart_item.quantity += 1
                    cart_item.save()
            return JsonResponse({
                "status":200,
                "message":"Item added"
            })
        else:
            return redirect("home")

@require_http_methods(["POST"])
def remove_from_cart(request):
    if request.method == "POST":
        curr_user = request.user

        data = json.loads(request.body)
        item_id = data.get('productId')

        cart, created = Cart.objects.get_or_create(user=curr_user)
        item = get_object_or_404(CartItem, pk=item_id)

        if curr_user.is_authenticated:
            item.delete()
            new_total_price = sum(item.quantity * item.product.price for item in cart.items.all())

            code_id = request.session.get('coupon_id')


            new_total_price_disc = False
            if code_id:
                coupon = Coupon.objects.get(id=code_id)
                new_total_price_disc = (new_total_price * coupon.discout/100)


            return JsonResponse({
                "status":200,
                "message":"Item removed",
                "new_total_price": new_total_price,
                "new_total_price_disc": new_total_price_disc,
            })
        else:
            return redirect("home")

@require_http_methods(["POST"])
def reset_cart(request):

    if request.method == "POST":
        curr_user = request.user
        cart, created = Cart.objects.get_or_create(user=curr_user)

        if curr_user.is_authenticated:
            for item in cart.items.all():
                item.delete()
            return JsonResponse({
                "status":200,
                "message":"Items removed",
            })
        else:
            return redirect("home")

@require_http_methods(["POST"])
def update_cart(request):
    """
    id - CartItem ID
    value - new value, when user change quantity of items
    """

    if request.method == "POST":
        curr_user = request.user

        data = json.loads(request.body)
        cart_item_id = data.get('cartItemID')
        new_val_of_quan = data.get('newValueOfQuantity')

        item = get_object_or_404(CartItem, pk=cart_item_id)
        cart, created = Cart.objects.get_or_create(user=curr_user)
        if curr_user.is_authenticated:

            item.quantity = int(new_val_of_quan)
            item.save()
            new_item_price = (item.quantity * item.product.price)
            new_total_price = sum(item.quantity * item.product.price for item in cart.items.all())

            return JsonResponse({
                "status":200,
                "message":"Item changed",
                "new_item_price": new_item_price,
                "new_total_price": new_total_price,
            })
        else:
            return redirect("home")

def checkout(request):

    code_id = request.session.get('coupon_id')

    curr_user = request.user
    user_prod = CartItem.objects.filter(user=curr_user)
    user_cart = Cart.objects.get(user=curr_user)

    total_price = sum(item.quantity * item.product.price for item in user_cart.items.all())
    
    context = {
        "curr_user" : curr_user,
        "user_prod" : user_prod,
        "total_price" : total_price,
    }

    if code_id:
        coupon = Coupon.objects.get(id=code_id)
        context['code'] = coupon
        context['total_price'] = total_price
        context['total_price_disc'] = (total_price * coupon.discout)/100

    return render(request, 'cart/checkout.html', context)

##@require_http_methods(["POST"])
def checkout_summary(request):
    code_id = request.session.get('coupon_id')
    user_profile = request.user.profile

    address = Address.objects.filter(profile=user_profile, type=1).first() ## Billing
    delivery = Address.objects.filter(profile=user_profile, type=2).first() ## Delivery

    cart_obj = Cart.objects.get(user=request.user)
    total_price = sum(item.quantity * item.product.price for item in cart_obj.items.all())

    context = {
        "cart":cart_obj,
        "total_price": total_price,
        "user_profile": user_profile,
        "address": address,
        "delivery": delivery,
    }

    if code_id:
        coupon = Coupon.objects.get(id=code_id)
        context['code'] = coupon
        context['total_price'] = total_price
        context['savings'] = total_price - (total_price * coupon.discout)/100
        context['total_price_disc'] = (total_price * coupon.discout)/100

    return render(request, "cart/checkout-1.html", context)
import json

from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse

from coupons.models import Coupon
from cart.models import Cart
# Create your views here.

def apply(request):
    now = timezone.now()
    data = json.loads(request.body)
    code = data.get('code')

    code_id = request.session.get('coupon_id')

    try:
        coupon = Coupon.objects.get(
            code__iexact = code,
            valid_from__lte=now,
            valid_to__gte=now,
            active=True
        )
        request.session['coupon_id'] = coupon.id

        user_cart = Cart.objects.get(user=request.user)
        new_price = sum(item.quantity * item.product.price for item in user_cart.items.all())

        return JsonResponse({
        "status":200,
        "message": f"Discount %{coupon.discout} active",
        "new_price" :  (new_price * coupon.discout) / 100,
        "old_price" : new_price,
        })

    except Coupon.DoesNotExist:
        
        request.session['coupon_id'] = None

        if code_id:
            request.session['coupon_id'] = code_id

        return JsonResponse({
            "status":401,
            "message": "Invalid",
        })

def remove(request):
    user_cart = Cart.objects.get(user=request.user)
    old_price = sum(item.quantity * item.product.price for item in user_cart.items.all())
    if request.session['coupon_id']:
        request.session['coupon_id'] = None

    return JsonResponse({
            "status":200,
            "message": "Code removed",
            "old_price": old_price,
        })
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.product} - {self.user}'

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)

    def __str__(self):
        return f'{self.user} Cart'

    # @staticmethod
    # def new_or_get( request):
    #     cart_id = request.session.get("cart_id", None)
    #     qs = Cart.objects.filter(id=cart_id)

    #     if qs.exists():
    #         cart_obj = qs.first()
    #         if request.user.is_authenticated and cart_obj.user is None:
    #             cart_obj.user = request.user
    #             cart_obj.save()
    #     else:
    #         cart_obj = Cart.objects.create(user=request.user if request.user.is_authenticated else None)
    #         request.session['cart_id'] = cart_obj.id

    #     return cart_obj

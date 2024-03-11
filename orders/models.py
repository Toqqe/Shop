from django.db import models

from accounts.models import Profile
from cart.models import CartItem
# Create your models here.

class Order(models.Model):
    ORD_STATUS =[
        (1, "New"),
        (2, "Waiting for payment"),
        (3, "Paid"),
        (4, "Canceled"),
        (5, "Ended"),
    ]

    PAYMENT_METHod = [
        (1, "BLIK"),
        (2, "PayPal"),
        (3, "Card"),
    ]

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    date_ordered = models.DateTimeField(auto_now_add=True)
    sum = models.DecimalField(default=0,decimal_places=2 , max_digits=10)
    status = models.IntegerField(choices=ORD_STATUS, default=1)
    payment = models.IntegerField(choices=PAYMENT_METHod)
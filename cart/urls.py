from django.urls import path

from . import views

urlpatterns = [
    path('cart-modal/', views.cart_modal , name="cart-modal"),
    path('add-to-cart/', views.add_to_cart , name="add-to-cart"),
    path('remove-from-cart/', views.remove_from_cart , name="remove-from-cart"),
    path('reset-cart/', views.reset_cart , name="restart-cart"),
    path('update-cart/', views.update_cart, name="update-cart"),

    path('checkout/', views.checkout, name="checkout"),
    path('checkout-1/', views.checkout_summary, name="checkout-1")

    ##path('cart/update', ,name="cart-update"),

]

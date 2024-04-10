from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from orders.views import get_orders as account_views_order
from .forms import LoginForm

urlpatterns = [
    path('', views.AccountView.as_view(), name="account"),
    path('orders/', account_views_order, name="orders"),
    # path('', views.accountView, name="account"),


    path('register/', views.RegisterView.as_view(), name="register-page"),
    path("login/", views.CustomLoginView.as_view(), name="login-page"),
    path('logout/', auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name="logout-page"),
    
]

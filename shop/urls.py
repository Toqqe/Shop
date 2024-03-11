from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings 


urlpatterns = [
    path('', views.index, name="home"),
    path('products/', views.ProductsView.as_view(), name="products-page"),
    
    path('products/<str:ordbdy>', views.ProductsView.as_view(), name="sort-products-page"),

    path('products/<str:category>/', views.ProductsView.as_view(), name="filter-product-page"),
    path('products/<str:category>/<str:ordbdy>', views.ProductsView.as_view(), name="filter-product-page"),

]

from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings 


urlpatterns = [
    path('', views.index, name="home"),
    path('products/', views.ProductsView.as_view(), name="products-page"),
    path('products/<slug:slug>/', views.product_detail_view, name="product-detail"),
    
    path('products/?ordby=<str:ordbdy>/', views.ProductsView.as_view(), name="sort-products-page"),

    path('products/filter=<str:category>/', views.ProductsView.as_view(), name="filter-product-page"),
    path('products/filter=<str:category>/?ordby=<str:ordbdy>/', views.ProductsView.as_view(), name="filter-product-page"),

]

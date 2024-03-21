from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404

from shop.models import Product, Category

# Create your views here.


def index(request):
    curr_user = request.user
    products = Product.objects.all().order_by('-id')[:3]

    """
    - produkty na głównej
    - slider,
    - użytkownik bar,
    - 
    """
    context = {
        "curr_user" : curr_user,
        "last_products": products
    }
    return render(request, "shop/index.html", context)


def sortProducts(ordby_value, category=None):

    if category:
        if ordby_value == "1":
            products = Product.objects.filter(category=category).order_by('price')[:20]
            print(products)
        elif ordby_value == "2":
            products = Product.objects.filter(category=category).order_by('-price')[:20]
        return products

    if ordby_value == "1":
        products = Product.objects.all().order_by('price')[:20]
    elif ordby_value == "2":
        products = Product.objects.all().order_by('-price')[:20]


    return products


class ProductsView(View):
    def get(self, request, category=None):
        curr_user = request.user
        products = Product.objects.all().order_by('-id')
        categories = Category.objects.all()
        choosed_category = ""

        if category:
            choosed_category = Category.objects.get(name=category)
            products = Product.objects.filter(category=choosed_category).order_by('-id')
            
        ordby_value = request.GET.get('ordby', None)
        if ordby_value:
            if ordby_value == "1":
                products = products.order_by('-price')
            elif ordby_value == "2":
                products = products.order_by('price')

            context = {
            "curr_user" : curr_user,
            "list_products": products,
            "categories": categories,
            "curr_category": choosed_category,
            }
            return render(request, 'shop/includes/product_list_items.html', context)

        context ={
            "curr_user" : curr_user,
            "list_products": products,
            "categories": categories,
            "curr_category": choosed_category,
        }

        return render(request, "shop/products_list.html", context)    
    

    def post(self, request):
        pass        
    
        # ordby_value = request.GET.get('ordby', None)
        # if ordby_value:
            
        #     products_template_name = "shop/includes/product_list_items.html"
        #     sorted_products = sortProducts(ordby_value, category)
        #     context = {
        #         "curr_user" : curr_user,
        #         "list_products": sorted_products,
        #         "categories": categories,
        #     }
        #     return render(request, products_template_name, context)
    
def product_detail_view(request, slug):

    product = get_object_or_404(Product, slug=slug)


    context = {
        "product":product
    }
    return render(request, "shop/product_view.html", context)

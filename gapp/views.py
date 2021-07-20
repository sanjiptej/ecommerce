from store.models import Product
from django.shortcuts import render
# from django.views import View
from store.models import Product

# Create your views here.

def gapp(request):
    products = Product.objects.all().filter(is_available=True)
    # product_count = products.count()

    context = {
        'products': products,
        # 'Product_count': product_count,
    }
    

    return render (request,'home.html',context)
    
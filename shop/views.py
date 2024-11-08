from django.shortcuts import render, HttpResponse
from .models import Product, Order
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    products = Product.objects.all()
    item_name = request.GET.get('item_name')
    if item_name != "" and item_name != None:
            products = products.filter(name__icontains=item_name)
    else:
          item_name = ""
    
    # paginator code
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request, 'shop/index.html', {"products": products, "item_name": item_name})

def detail(request, id):
      product = Product.objects.get(pk=id)
      property(product.name)
      return render(request, 'shop/detail.html', {"product": product})

def cart(request):
      if request.method == 'POST':
            items = request.POST.get('items')
            name = request.POST.get('name')
            email = request.POST.get('email')
            address = request.POST.get('address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            zip_code = request.POST.get('zip_code')
            total = request.POST.get('amount-to-pay')

            print('name:', name, '\nitems:', items, '\nemail=', email, '\naddress=', address,
                  '\city=', city, '\nstate', state, '\nzip_code', zip_code, '\ntotal=', total)

            order = Order(items=items, name=name, email=email, address=address, city=city, state=state, zip_code=zip_code, total=total)
            order.save()

      return render(request, 'shop/cart.html')


from django.shortcuts import redirect, render
from .models import Product
from .forms import CreateProductForm



def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'sale/index.html', context)


def create_product(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        print(111)
        if form.is_valid():
            print(222)
            form.save()
            print(333)
            return redirect('/')
    else:  
        form = CreateProductForm()

    context = {'form': form}
    return render(request, 'sale/create_product.html', context=context)


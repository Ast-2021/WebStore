
from django.shortcuts import redirect, render
from .models import Product, Category
from .forms import CreateProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required



def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, 'sale/index.html', context)


@login_required(login_url='login')
def create_product(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save()
            new_product.author = request.user
            new_product.save()
            return redirect('home')
    else:  
        form = CreateProductForm()
    context = {'form': form}
    return render(request, 'sale/create_product.html', context=context)


def page_product(request, prod_pk):
    product = Product.objects.get(pk=prod_pk)
    context = {'product': product}
    return render(request, 'sale/page_product.html', context=context)


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = UserCreationForm()
    return render(request, 'sale/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('home')
        else:
            messages.error(request,'username or password not correct')
        return render(request, 'sale/login.html', {'form':form})
        
                
    else:
        form = AuthenticationForm()
    return render(request, 'sale/login.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect('home')


def delete_product(request, prod_pk):
    Product.objects.get(pk=prod_pk).delete()
    return redirect('home')


def update_product(request, prod_pk):
    product = Product.objects.filter(pk=prod_pk)[0]
    form = CreateProductForm({
        'title': product.title,
        'description': product.description,
        'category': product.category,
        'author': product.author,
        'phone_number': product.phone_number,
        'price': product.price
    })
    if request.method == 'POST':
        if form.is_valid():
            product.title = request.POST['title']
            product.description = request.POST['description']
            product.category = Category.objects.get(pk=request.POST['category'])
            product.author = User.objects.get(pk=request.POST['author'])
            product.phone_number = request.POST['phone_number']
            product.price = request.POST['price']
            product.save()

            return redirect('home')
    context = {'form': form}
    return render(request, 'sale/update_product.html', context=context)


def category_page(request, cat_pk):
    categories = Category.objects.all()
    category = Category.objects.get(pk=cat_pk)
    products = Product.objects.filter(category=category)
    context = {'products': products, 'categories': categories}
    return render(request, 'sale/index.html', context=context)


def form_search(request):
    search = request.POST.get('search')
    products = Product.objects.filter(title=search)
    context = {'products': products}
    return render(request, 'sale/index.html', context=context)
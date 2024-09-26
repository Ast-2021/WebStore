
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Product, Category
from .forms import CreateProductForm
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'sale/index.html', context)


@login_required
def create_product(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save()
            new_product.author = request.user
            new_product.save()
            return redirect('/')
    else:  
        form = CreateProductForm()

    context = {'form': form}
    return render(request, 'sale/create_product.html', context=context)


def page_product(request, prod_pk):
    product = Product.objects.get(pk=prod_pk)
    context = {'product': product}
    return render(request, 'sale/page_product.html', context=context)


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'sale/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'sale/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def user_logout(request):
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
        'author': product.author
    })
    if request.method == 'POST':
        if form.is_valid():
            print('andand', request.POST['category'])
            product.title = request.POST['title']
            product.description = request.POST['description']
            product.category = Category.objects.get(pk=request.POST['category'])
            product.author = User.objects.get(pk=request.POST['author'])
            product.save()

            return redirect('home')
    context = {'form': form}
    return render(request, 'sale/update_product.html', context=context)


from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('create_product/', create_product, name='create_product'),
    path('product/<int:prod_pk>', page_product, name='page_product'),
    path('register', register_view, name='register'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('delete_product/<int:prod_pk>', delete_product, name='delete_product'),
    path('update/<int:prod_pk>', update_product, name='update_product'),
    path('category/<int:cat_pk>', category_page, name='category'),
    path('form_search/', form_search, name='form_search'),
    path('help', help_view, name='help'),
    path('about', help_view, name='about'),
    path('user_page', user_page, name='user_page')
]


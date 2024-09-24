from django.urls import resolve
from .views import index
from .models import Product, Category, User
from .forms import CreateProductForm

from django.test import TestCase


class HomePageTest(TestCase):
    """Home page tests"""


    def test_index_function_work(self):
        """Checking the index function"""

        found = resolve('/')
        response = self.client.get('/')

        self.assertEqual(found.func, index)
        self.assertTemplateUsed(response, 'sale/index.html')
        self.assertEqual(response.status_code, 200)


    def test_output_data_from_model_to_home_page(self):
        """checking the output of data from the model to the home page"""

        category = Category.objects.create(title='Clothes')
        author = User.objects.create(username='John', email='random@gmail.com', password='password')
        product = Product.objects.create(title='First', category=category, author=author)

        response = self.client.get('/')

        self.assertIn(product.title, response.content.decode('utf-8'))


class ModelsTest(TestCase):
    """testing models for functionality"""


    def test_product_model(self):
        """Checking the operation of the product module"""

        category = Category.objects.create(title='Clothes')
        author = User.objects.create(username='John', email='random@gmail.com', password='password')


        Product.objects.create(title='First', category=category, author=author)
        Product.objects.create(title='Second', category=category, author=author)
        Product.objects.create(title='Third', category=category, author=author)

        self.assertEqual(Product.objects.count(), 3)
        self.assertEqual(Product.objects.first().title, 'First')


    def test_user_model(self):
        """Checking the creation of User model instances"""

        User.objects.create(username='John', email='random@gmail.com', password='password')

        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username, 'John')


class PageForPostingAnProducts(TestCase):
    """page for posting items for sale"""

    def test_form_create_product(self):

        category = Category.objects.create(title='Clothes')
        author = User.objects.create(username='John', email='random@gmail.com', password='password')

        form_data = {'title': 'Avatar', 'category': category, 'author': author}
        form = CreateProductForm(data=form_data)
        self.assertTrue(form.is_valid())


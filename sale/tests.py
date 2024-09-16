from django.urls import resolve
from .views import index
from .models import Product, Category

from django.test import TestCase


class HomePageTest(TestCase):
    """ First Tests """


    def test_index_function_work(self):
        """Checking the index function"""

        found = resolve('/')
        response = self.client.get('/')

        self.assertEqual(found.func, index)
        self.assertTemplateUsed(response, 'sale/index.html')
        self.assertEqual(response.status_code, 200)


    def test_product_model(self):
        """Checking the operation of the product module"""

        category = Category.objects.create(title='Clothes')

        Product.objects.create(title='First', phone=8, category=category)
        Product.objects.create(title='Second', phone=7, category=category)
        Product.objects.create(title='Third', phone=7, category=category)

        self.assertEqual(Product.objects.count(), 3)
        self.assertEqual(Product.objects.first().title, 'First')


    def test_output_data_from_model_to_home_page(self):
        """checking the output of data from the model to the home page"""

        category = Category.objects.create(title='Clothes')
        product = Product.objects.create(title='First', phone=8, category=category)

        response = self.client.get('/')

        self.assertIn(product.title, response.content.decode('utf-8'))


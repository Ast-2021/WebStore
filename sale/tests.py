from django.urls import resolve
from .views import index
from .models import Product, Category

from django.test import TestCase


class FirstsTest(TestCase):
    """ First Tests """

    def test_index_work(self):
        """ check the work of the index function """

        found = resolve('/')
        response = self.client.get('/')

        self.assertEqual(found.func, index)
        self.assertTemplateUsed(response, 'sale/index.html')
        self.assertEqual(response.status_code, 200)

    def test_product_model(self):
        """ test product model """

        category = Category.objects.create(title='Одежда')

        first = Product.objects.create(title='First', phone=8, category=category)
        second = Product.objects.create(title='Second', phone=7, category=category)
        third = Product.objects.create(title='Third', phone=7, category=category)


        self.assertEqual(Product.objects.count(), 3)
        self.assertEqual(Product.objects.first().title, 'First')

    def test_product_view(self):
        """jjj"""

        category = Category.objects.create(title='Техника')

        first = Product.objects.create(title='Космический корабль', phone=7, category=category)

        response = self.client.get('/')








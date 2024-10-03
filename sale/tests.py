from django.urls import reverse
from .models import Product, Category, User

from django.test import TestCase, Client


class TestViews(TestCase):
    """Тестирование классов и функций модуля views.py"""

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(title='test_category')
        self.category_2 = Category.objects.create(title='test_category_2')
        self.user = User.objects.create_user(username='username', password='password')
        self.product = Product.objects.create(title='test_product', 
                                              description='hello', 
                                              author=self.user, 
                                              category=self.category, 
                                              phone_number=79999999999, 
                                              price='125000')  
              
        self.client.login(username='username', password='password')

        self.url_page_product = reverse('page_product', args=[self.product.pk])
        self.url_register = reverse('register')
        self.url_login = reverse('login')
        self.url_update_product = reverse('update_product', args=[self.product.pk])
        self.url_delete_product = reverse('delete_product', args=[self.product.pk])
        self.url_logout = reverse('logout')
        self.url_category_page = reverse('category', args=[self.category_2.pk])
        self.url_create_product = reverse('create_product')
        self.url_form_search = reverse('form_search')


    def test_index_GET(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertIn('test_category', response.content.decode('utf-8'))
        self.assertIn('test_product', response.content.decode('utf-8'))
        self.assertTemplateUsed(response, 'sale/index.html')


    def test_create_product_with_wrong(self):
        response = self.client.post(self.url_create_product, {'title': 'wrong'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Product.objects.count(), 1)


    def test_create_product(self):
        response = self.client.post(self.url_create_product, {
            'title': 'test_product_2', 
            'description': 'hi',
            'author': str(self.user.pk), 
            'category': str(self.category.pk),
            'phone_number': '79999999999',
            'price': '24900',
            })


        self.assertEqual(response.status_code, 302)
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(Product.objects.last().title, 'test_product_2')


    def test_update_product(self):
        response = self.client.post(self.url_update_product, {
            'title': 'Update_test_title',
            'description': 'welcome', 
            'author': str(self.user.pk), 
            'category': str(self.category.pk),
            'phone_number': '79999999999',
            'price': '1000000',
            })
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Product.objects.first().title, 'Update_test_title')
        self.assertEqual(Product.objects.count(), 1)


    def test_delete_product(self):
        response = self.client.get(self.url_delete_product)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Product.objects.count(), 0)


    def test_page_product(self):
        response = self.client.get(self.url_page_product)

        self.assertEqual(response.status_code, 200)
        self.assertIn('test_product', response.content.decode('utf-8'))
        self.assertTemplateUsed(response, 'sale/page_product.html')


    def test_register_view(self):
        self.client.logout()
        response = self.client.post(self.url_register, data={
            'username': 'username_2', 
            'password1': 'rekmcfhby',
            'password2': 'rekmcfhby',
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 2)

    
    def test_login_view(self):
        self.client.logout()
        response = self.client.post(self.url_login, data={
            'username': 'username',
            'password': 'password'
        })

        self.assertEqual(response.status_code, 302)

    
    def test_logout_view(self):
        response = self.client.get(self.url_logout)

        self.assertEqual(response.status_code, 302)

        
    def test_category_page(self):
        product_2 = Product.objects.create(title='clothes',
                                              description='hello', 
                                              author=self.user, 
                                              category=self.category_2, 
                                              phone_number=79999999999, 
                                              price='125000') 

        response = self.client.get(self.url_category_page)

        self.assertEqual(response.status_code, 200)
        self.assertIn(product_2.title, response.content.decode('utf-8'))
        self.assertNotIn(self.product.title, response.content.decode('utf-8'))


    def test_form_search(self):
        product_2 = Product.objects.create(title='clothes',
                                              description='hello', 
                                              author=self.user, 
                                              category=self.category_2, 
                                              phone_number=79999999999, 
                                              price='125000')
        
        response = self.client.post(self.url_form_search, data={
            'search': 'clothes'
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn(product_2.title, response.content.decode('utf-8'))
        self.assertNotIn(self.product.title, response.content.decode('utf-8'))



class TestModels(TestCase):
    """Тестирование моделей модуля models.py"""

    def setUp(self):
        self.category = Category.objects.create(title='test_category')
        self.user = User.objects.create_user(username='username', password='password')

    
    def test_product_model(self):
        product = Product.objects.create(title='test_product', 
                                         description='hello', 
                                         author=self.user, 
                                         category=self.category, 
                                         phone_number=79999999999, 
                                         price='125000')

        self.assertEqual(str(product), 'test_product')
        self.assertTrue(isinstance(product, Product))
    
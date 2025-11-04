from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from products.models import Product, Review

User = get_user_model()


class TestRoutes(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create(username='Лев Толстой')
        cls.reader = User.objects.create(username='Читатель простой')
        cls.product = Product.objects.create(name='Название', text='Текст', author=cls.author)
        cls.review = Review.objects.create(
            text='Текст отзыва',
            estimation=4,
            product=cls.product,
            author=cls.author
        )

    def test_pages_availability(self):
        """Проверка доступности страниц."""
        urls = (
            ('api:product-list', None),
            ('api:product-detail', (self.product.id,)),
            ('api:review-list', (self.product.id,)),
            ('api:review-detail', (self.review.product.id, self.review.id)),
        )
        for name, args in urls:
            with self.subTest(name=name):
                url = reverse(name, args=args)
                response = self.client.get(url)
                self.assertEqual(response.status_code, HTTPStatus.OK)
    
    def test_availability_for_product__edit_and_delete(self):
        """
        Проверка доступности страницы редактирования
        и удаления товара автору/читателю.
        """
        client = APIClient()
        product_data = {
            'name': self.product.name,
            'text': self.product.text,            
        }
        users_methods_statuses = (
            (self.author, 'PUT', HTTPStatus.OK),
            (self.author, 'PATCH', HTTPStatus.OK),
            (self.author, 'DELETE', HTTPStatus.NO_CONTENT),
            (self.reader, 'PUT', HTTPStatus.NOT_FOUND),
            (self.reader, 'PATCH', HTTPStatus.NOT_FOUND),
            (self.reader, 'DELETE', HTTPStatus.NOT_FOUND),
        )
        for user,  method, status in users_methods_statuses:
            client.force_authenticate(user=user)
            url = reverse('api:product-detail', args=(self.product.id,))
            with self.subTest(user=user, method=method):
                if method == 'PUT':
                    response = client.put(
                        url,
                        data=product_data,
                        format='json'
                    )
                elif method == 'PATCH':
                    response = client.patch(
                    url, 
                    data={'name': 'Новое'},
                        format='json'
                    )
                elif method == 'DELETE':
                    response = client.delete(url)
                self.assertEqual(response.status_code, status)
    
    def test_availability_for_review__edit_and_delete(self):
        """
        Проверка доступности страницы редактирования
        и удаления отзыва автору/читателю.
        """
        client = APIClient()
        review_data = {
            'estimation': self.review.estimation,
            'text': self.review.text,       
        }
        users_methods_statuses = (
            (self.author, 'PUT', HTTPStatus.OK),
            (self.author, 'PATCH', HTTPStatus.OK),
            (self.author, 'DELETE', HTTPStatus.NO_CONTENT),
            (self.reader, 'PUT', HTTPStatus.NOT_FOUND),
            (self.reader, 'PATCH', HTTPStatus.NOT_FOUND),
            (self.reader, 'DELETE', HTTPStatus.NOT_FOUND),
        )
        for user,  method, status in users_methods_statuses:
            client.force_authenticate(user=user)
            url = reverse('api:review-detail', args=(self.review.product.id, self.review.id))
            with self.subTest(user=user, method=method):
                if method == 'PUT':
                    response = client.put(
                        url,
                        data=review_data,
                        format='json'
                    )
                elif method == 'PATCH':
                    response = client.patch(
                    url, 
                    data={'text': 'Новое'},
                        format='json'
                    )
                elif method == 'DELETE':
                    response = client.delete(url)
                self.assertEqual(response.status_code, status)

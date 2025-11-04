from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from products.models import Product, Review

User = get_user_model()

class TestProductCreation(TestCase):
    PRODUCT_NAME = 'Наим. товара'
    PRODUCT_TEXT = 'Текст товара'

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='Мимо Крокодил')
        cls.auth_client = APIClient()
        cls.auth_client.force_authenticate(user=cls.user)
        cls.url = reverse('api:product-list')
        cls.form_data = {'text': cls.PRODUCT_TEXT, 'name': cls.PRODUCT_NAME}

    def test_anonymous_user_cant_create_product(self):
        """Проверка создания товара анонимным пользователем."""  
        self.client.post(self.url, data=self.form_data)
        products_count = Product.objects.count()
        self.assertEqual(products_count, 0)
    
    def test_user_can_create_product(self):
        """
        Проверка создания товара авторизированным пользователем.
        """
        products_count_before = Product.objects.count()
        response = self.auth_client.post(self.url, data=self.form_data, format='json')
        self.assertEqual(response.status_code, 201)
        products_count_after = Product.objects.count()
        self.assertEqual(products_count_after, products_count_before + 1)

class TestReviewEditDelete(TestCase):
    REVIEW_TEXT = 'Текст отзыва'
    NEW_REVIEW_TEXT = 'Новый текст'

    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create(username='Автор товара')
        cls.author_client = APIClient()
        cls.author_client.force_authenticate(cls.author)
        cls.reader = User.objects.create(username='Читатель')
        cls.reader_client = APIClient()
        cls.reader_client.force_authenticate(cls.reader)
        cls.product = Product.objects.create(name='Наименование', text='Текст', author=cls.author)
        products_url = reverse('api:product-detail', args=(cls.product.id,))
        cls.url_to_reviews = products_url + '#reviews'
        cls.review = Review.objects.create(
            product=cls.product,
            author=cls.author,
            estimation=5,
            text=cls.REVIEW_TEXT
        )
        cls.edit_and_delete_url = reverse('api:review-detail', args=(cls.product.id, cls.review.id,)) 
        cls.form_data = {'text': cls.NEW_REVIEW_TEXT}

    def test_author_can_delete_review(self):
        """Проверка удаления отзыва автором."""
        reviews_count = Review.objects.count()
        response = self.author_client.delete(self.edit_and_delete_url)
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)
        self.assertEqual(Review.objects.count(), reviews_count - 1)
    
    def test_reader_cannot_delete_review(self):
        """Проверка, что пользователь не может удалить чужой отзыв."""
        reviews_count = Review.objects.count()
        response = self.reader_client.delete(self.edit_and_delete_url)
        self.assertIn(response.status_code, [HTTPStatus.FORBIDDEN, HTTPStatus.NOT_FOUND])
        self.assertEqual(reviews_count, 1)
    
    def test_author_can_edit_review(self):
        """Проверка редактирования отзыва автором."""
        response = self.author_client.patch(
            self.edit_and_delete_url, 
            data=self.form_data, 
            format='json'
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.review.refresh_from_db()
        self.assertEqual(self.review.text, self.NEW_REVIEW_TEXT)
    
    def test_reader_cannot_edit_review(self):
        """Проверка, что пользователь не может редактировать чужой отзыв."""
        response = self.reader_client.patch(
            self.edit_and_delete_url, 
            data=self.form_data, 
            format='json'
        )
        self.assertIn(response.status_code, [HTTPStatus.FORBIDDEN, HTTPStatus.NOT_FOUND])

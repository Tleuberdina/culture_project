from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .constants import MAX_VALUE, MIN_VALUE


User = get_user_model()


class Product(models.Model):
    name = models.CharField(verbose_name='Название товара', max_length=16)
    text = models.TextField(verbose_name='Описание товара')
    author = models.ForeignKey(
        User,
        verbose_name='Автор товара',
        on_delete=models.CASCADE, related_name='products'
    )
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True)
    image = models.ImageField(
        upload_to='cats/images/', 
        null=True,  
        default=None
        )
    
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField(verbose_name='Текст отзыва')
    estimation = models.PositiveSmallIntegerField(
        verbose_name='Оценка товара',
        default=5,
        validators=[MinValueValidator(MIN_VALUE),
                    MaxValueValidator(MAX_VALUE)],
        error_messages={
            'min_value': 'Значение меньше 1.',
            'max_value': 'Значение больше 5.'
        }
    )
    product = models.ForeignKey(
        Product,
        verbose_name='Товар',
        related_name='reviews',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор отзыва',
        on_delete=models.CASCADE, related_name='reviews'
    )
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True)
    
    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text

from django.db.models import Avg
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

from .permissions import AuthorOrReadOnly
from .serializers import ProductSerializer, ReviewSerializer
from products.models import Product, Review



class ReviewViewSet(viewsets.ModelViewSet):
    """Обрабатывает операции CRUD для модели Review."""
    serializer_class = ReviewSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = PageNumberPagination

    def get_product(self):
        return get_object_or_404(Product, id=self.kwargs['product_id'])

    def get_queryset(self):
        product = self.get_product()
        return product.reviews.all()

    def perform_create(self, serializer):
        product = self.get_product()
        serializer.save(
            author=self.request.user,
            product=product
        )


class ProductViewSet(viewsets.ModelViewSet):
    """Обрабатывает операции CRUD для модели Product."""
    queryset = Product.objects.annotate(
        average_score=Avg('reviews__estimation')
    )
    serializer_class = ProductSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = None
    filterset_fields = ('name',)
    search_fields = ('name',)
    ordering_fields = ('name',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

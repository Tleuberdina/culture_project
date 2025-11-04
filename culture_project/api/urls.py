from rest_framework import routers
from django.urls import include, path

from .views import ProductViewSet, ReviewViewSet


app_name = 'api'
v1_router = routers.DefaultRouter()
v1_router.register('products', ProductViewSet, basename='product')
v1_router.register(
    r'products/(?P<product_id>\d+)/reviews',
    ReviewViewSet,
    basename='review'
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
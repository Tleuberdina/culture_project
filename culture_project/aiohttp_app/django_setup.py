import os
import sys
import django
from asgiref.sync import sync_to_async


project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'culture_project.settings')
django.setup()

from products.models import Product
from api.serializers import ProductSerializer


@sync_to_async
def get_all_products():
    """Получаем продукты."""
    return list(Product.objects.all())

@sync_to_async
def get_product_by_id(product_id):
    """Получаем один продукт."""
    try:
        return Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return None

@sync_to_async
def serialize_products(products):
    """Сериализация продуктов."""
    serializer = ProductSerializer(products, many=True)
    return serializer.data

@sync_to_async
def serialize_product(product):
    """Сериализация одного продукта."""
    serializer = ProductSerializer(product)
    return serializer.data

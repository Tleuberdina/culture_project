import os
import sys
import django
from aiohttp import web


project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'culture_project.settings')
django.setup()

from aiohttp_app.django_setup import (
    get_all_products, get_product_by_id, serialize_products, serialize_product
)


async def handle_products(request):
    """Получаем асинхронно все продукты из БД Django."""
    try:
        products = await get_all_products()
        serialized_data = await serialize_products(products)
        return web.json_response({
            'status': 'success',
            'count': len(serialized_data),
            'products': serialized_data
        })
    except Exception as e:
        return web.json_response({
            'status': 'error',
            'message': str(e)
        }, status=500)

async def handle_product_detail(request):
    """Получаем асинхронно конкретный продукт по ID из БД Django."""
    try:
        product_id = int(request.match_info['product_id'])
        product = await get_product_by_id(product_id)
        if product is None:
            return web.json_response({
                'status': 'error',
                'message': f'Продукт с id {product_id} не найден.'
            }, status=404)
        serialized_data = await serialize_product(product)
        return web.json_response({
            'status': 'success',
            'product': serialized_data
        })
    except ValueError:
        return web.json_response({
            'status': 'error',
            'message': 'Неверный id продукта.'
        }, status=400)
    except Exception as e:
        return web.json_response({
            'status': 'error', 
            'message': str(e)
        }, status=500)


app = web.Application()

app.router.add_get('/products', handle_products)
app.router.add_get('/products/{product_id:\d+}', handle_product_detail)

if __name__ == '__main__':
    web.run_app(app, host='localhost', port=8080)

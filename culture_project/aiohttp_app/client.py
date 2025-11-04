import aiohttp
import asyncio
import time

async def test_server():
    """Тестируем сервер с БД Django."""
    async with aiohttp.ClientSession() as session:
        endpoints = [
            ('/products', 'All Products'), 
            ('/products/1', 'Product 1'),
            ('/products/2', 'Product 2')
        ]
        for endpoint, name in endpoints:
            try:
                start_time = time.time()
                url = f'http://localhost:8080{endpoint}'
                async with session.get(url) as response:
                    data = await response.json()
                    elapsed = time.time() - start_time
                    print(f'\n{name}:')
                    print(f'URL: {url}')
                    print(f'Статус: {response.status}')
                    print(f'Время: {elapsed:.2f}s')
                    print(f'Ответ: {data}')
                    
            except Exception as e:
                print(f'Проверка на наличие ошибок {name}: {e}')

if __name__ == '__main__':
    asyncio.run(test_server())

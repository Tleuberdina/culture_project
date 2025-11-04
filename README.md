### Описание:
Данный проект - платформа с возможностью регистрации пользователей; создавать, редактировать или удалить свой товар, а также оставить отзыв на товар.

### Технологии:
- Python
- Django REST Framework
- SQLite
- DJOSER
- aiohttp
- OpenAPI

### Документация проекта: http://localhost/redoc/

### Команда для запуска теста проекта: python manage.py test

## Шаги развертывания
1. Клонировать репозиторий и перейти в него в командной строке: git clone
2. Cоздать и активировать виртуальное окружение: python -m venv venv/source venv/Scripts/activate
3. Установить зависимости из файла requirements.txt: python -m pip install -- upgrade pip/pip install -r requirements.txt
4. Выполнить миграции: python manage.py migrate
5. Запустить проект: python manage.py runserver

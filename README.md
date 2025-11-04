## Описание:
Данный проект - платформа с возможностью регистрации пользователей; создавать, редактировать или удалить свой товар, а также оставить отзыв на товар.

### Технологии:
- Python
- Django REST Framework
- SQLite
- JWT + Djoser
- aiohttp
- OpenAPI
- Unittest

### Документация проекта: http://localhost/redoc/

### Команда для запуска теста проекта: python manage.py test

### Шаги развертывания
1. Клонировать репозиторий и перейти в него в командной строке: git clone git@github.com:Tleuberdina/culture_project.git
2. Cоздать и активировать виртуальное окружение:
   #### cd culture_project
   #### python -m venv venv/source venv/Scripts/activate
4. Установить зависимости из файла requirements.txt:
   #### python -m pip install -- upgrade pip
   #### pip install -r requirements.txt
6. Выполнить миграции: python manage.py migrate
7. Запустить проект: python manage.py runserver

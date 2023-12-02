#!/bin/bash

# устанавливаем необходимые зависимости
pip install -r requirements.txt

# выполняем миграции
python manage.py makemigrations
python manage.py migrate

# создаем администратора, если он еще не существует
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin') if not User.objects.filter(username='admin').exists() else 0;" | python manage.py shell

# запускаем сервер Django
python manage.py runserver
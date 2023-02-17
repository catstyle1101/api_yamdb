# Запуск проекта

- Клонируем репорзиторий
git clone ###

- Создаем виртуальное окружение
python -m venv venv 
venv/Scripts/activate

- Устанавливаем зависимости
pip install -r requirements.txt

- Перходим в папку с проектом
cd yatube_api

- Запускаем миграции
python manage.py makemigrations
python manage.py migrate

- Запускаем проект
python3 manage.py runserver
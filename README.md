# Описание проекта API_YaMDb

Данное API собирает отзывы пользователей на произведения. Произведения делятся на категории. Список категорий может быть расширен. Произведению может быть присвоен жанр из списка предустановленных.

Представленны следующие ресурсы:

 • Ресурс titles: произведения, к которым пишут отзывы (определённый фильм, книга или песенка).

 • Ресурс categories: категории (типы) произведений («Фильмы», «Книги», «Музыка»). Одно • произведение может быть привязано только к одной категории.

 • Ресурс genres: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.

 • Ресурс reviews: отзывы на произведения. Отзыв привязан к определённому произведению.

 • Ресурс comments: комментарии к отзывам. Комментарий привязан к определённому отзыву.

# Пользовательские роли и права доступа.
Добавлять произведения, категории и жанры может только администратор

 • Аноним — может просматривать описания произведений, читать отзывы и комментарии.

 • Аутентифицированный пользователь (user) — может читать всё, как и Аноним, может публиковать отзывы и ставить оценки произведениям (фильмам/книгам/песенкам), может комментировать отзывы; может редактировать и удалять свои отзывы и комментарии, редактировать свои оценки произведений. Эта роль присваивается по умолчанию каждому новому пользователю.

 • Модератор (moderator) — те же права, что и у Аутентифицированного пользователя, плюс право удалять и редактировать любые отзывы и комментарии.

 • Администратор (admin) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.

 • Суперюзер Django должен всегда обладать правами администратора, пользователя с правами admin. Даже если изменить пользовательскую роль суперюзера — это не лишит его прав администратора. Суперюзер — всегда администратор, но администратор — не обязательно суперюзер.

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

- Проект находиться по адресу http://localhost:8000/

# Регистрация новых пользователей

 • Пользователь отправляет POST-запрос с параметрами email и username на эндпоинт /api/v1/auth/signup/

  {
      "username": "####",
      "email": "####"
  }

 • Сервис YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на указанный адрес email.

  {
     "username": "####",
     "email": "####"
  }

 • Пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт /api/v1/auth/token/.

  {
      "username": "####",
      "confirmation_code": "####"
  }

 • В ответе на запрос ему приходит token (JWT-токен)

  {
      "token": "####"
  }

Примеры других запросов вы можите посотреть в документации к проекту по адресу
http://localhost:8000/redoc/

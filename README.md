В рамках учебного курсового проекта реализована бэкенд-часть SPA веб-приложения - трекер полезных привычек.

Приложение позволяет создавать, редактировать, удалять и просматривать Привычки. 
А так же получать напоминания о необходимости выполнить действие Привычки через мессенджер Телеграм.

Привычка - это действие, которое можно уложить в одно предложение:
я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]

Привычка может быть Полезной или Приятной.
Полезная привычка — это само действие, которое пользователь будет совершать и получать за его выполнение 
определенное вознаграждение (приятная привычка или любое другое вознаграждение).

Приятная привычка — это способ вознаградить себя за выполнение полезной привычки. Приятная привычка указывается 
в качестве связанной для полезной привычки.

Полезная привычка может иметь либо вознаграждение, либо связанную приятную привычку. 
У приятной привычки не может быть вознаграждения или связанной привычки.
Время выполнения привычки должно быть не больше 120 секунд.
Частота выполнения привычки от 1 до 7 дней, по умолчанию 1 день

Реализованы эндпоинты:
    Регистрация пользователя.
    Авторизация пользователя.
    Вывод списка привычек текущего пользователя с пагинацией (с выводом по 5 привычек на страницу).
    Вывод списка публичных привычек без возможности текущему пользователю их как-то редактировать или удалять.
    Создание привычки.
    Редактирование привычки.
    Удаление привычки.
    Просмотр привычки.


Реализована работа с отложенными задачами для напоминания о необходимости выполнить действие Привычки. 
(используется Celery)
Для рассылки уведомлений выполнена интеграция с мессенджером Телеграм.

Безопасность
Для проекта настроен CORS.

Документация доступна:
swagger/
redoc/



Для запуска проекта необходимо:
1. клонировать репозиторий: https://github.com/AnnaSobolevaV/DRF_course_work.git
2. установить окружение и зависимости (для управления зависимостями использован poetry.(см. pyproject.toml) )
3. файл с переменными окружения (.env.exmpl) необходимо заполнить и сохранить с именем .env
4. настроить базу данных и выполнить миграции
5. запустить Redis
6. запустить планировщик задач Celery: celery -A config worker --beat --scheduler django --loglevel=info


Для запуска проекта через Docker необходимо:
1. выполнить команду 
    docker-compose up -d --build  
2. после того как образ соберется и запустится контейнер с сервисами, успешность можно проверить командой:
    docker-compose ps 
с помощью которой можно увидеть запущенные сервисы:
NAME                            IMAGE                         COMMAND                  SERVICE       CREATED         STATUS                   PORTS
drf_course_work-celery-1        drf_course_work-celery        "celery -A config wo…"   celery        4 minutes ago   Up 3 minutes             
drf_course_work-celery-beat-1   drf_course_work-celery-beat   "celery -A config be…"   celery-beat   4 minutes ago   Up 3 minutes             
drf_course_work-db-1            postgres:16                   "docker-entrypoint.s…"   db            4 minutes ago   Up 4 minutes (healthy)   5432/tcp
drf_course_work-redis-1         redis:latest                  "docker-entrypoint.s…"   redis         4 minutes ago   Up 4 minutes             6379/tcp
drf_course_work-routine_app-1   drf_course_work-routine_app   "bash -c 'python man…"   routine_app   4 minutes ago   Up 3 minutes             0.0.0.0:8000->8000/tcp

3. так же можно запустить команду:
   docker-compose logs 
и убедиться что в логе нет ошибок.

4. для проверки работоспособности сервиса routine_app запустите:
     docker-compose exec routine_app bash -c python
- команда запустит Python, после чего необходимо набрать следующий код:

import requests
import json

url = "http://127.0.0.1:8000/users/register/"
payload = json.dumps({
  "password": "password_new",
  "email": "test@mail.ru"
})
headers = {
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)

- обработав запрос сервис выведет подобный результат:

{"id":2,"password":"pbkdf2_sha256$870000$J4ibKQWTUmSwkAqLsH7oqW$U/mUh8imUP5OCjez6cgUOWLc1lWn4DdHZsPbjQ238qU=","last_login":null,"is_superuser":false,"first_name":"","last_name":"","is_staff":false,"date_joined":"2025-03-04T20:13:10.467054Z","email":"test@mail.ru","phone":null,"avatar":null,"city":null,"token":null,"tg_id":null,"is_active":true,"groups":[],"user_permissions":[]}


5. для проверки работоспособности сервиса redis запустите:
     docker-compose exec redis redis-cli ping 
- в ответ получите:
PONG

6. для проверки работоспособности сервиса celery запустите команду:
      docker-compose exec celery python manage.py shell -c "from routine.tasks import test; test.delay()"

затем запустите docker-compose logs и убедитесь что в логе есть подобное сообщение:

celery-1       | [2025-03-05 11:15:59,574: INFO/MainProcess] celery@f4cbc9971ebb ready.
celery-1       | [2025-03-05 11:17:31,547: INFO/MainProcess] Task routine.tasks.test[ca597ba3-b3ad-45f9-8ee9-b119fdaa9789] received
celery-1       | [2025-03-05 11:17:31,551: WARNING/ForkPoolWorker-8] Test is completed
celery-1       | [2025-03-05 11:17:31,551: INFO/ForkPoolWorker-8] Task routine.tasks.test[ca597ba3-b3ad-45f9-8ee9-b119fdaa9789] succeeded in 0.0031679579988121986s: None



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

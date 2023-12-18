# Tiny Cloud

## Инструкция по установке на сервер

Приложение можно развернуть на сервере, поддерживающем docker.

Для установки понадобится порядка 1,5 Гб свободного дискового пространства для проекта, 
помимо места для установки [docker](https://docs.docker.com/engine/) и [docker-compose](https://docs.docker.com/compose/install/).

### Процеcc установки

##### Подготовка ПО:
1. Установите Docker: https://docs.docker.com/engine/
2. Установите Docker-compose: https://docs.docker.com/compose/install/
3. Установите Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
4. Клонируйте ветки `main` репозиториев проекта в одну папку так, чтобы они находились на одном уровне. 
Например, `~/tiny-cloud/liaksej-tiny-cloud-backend` и `~/tiny-cloud/liaksej-tiny-cloud-frontend`.

    ```shell
    git clone -b main https://github.com/Liaksej/liaksej-tiny-cloud-backend.git
    
    git clone -b main https://github.com/Liaksej/liaksej-tiny-cloud-frontend.git
    ```

##### Подготовка переменных окружения:
1. В директории `/liaksej-tiny-cloud-backend` на сервере откройте файл `.example.env`. Это файл с настройками
   для сервера Django. Откорректируйте нужные строки, приведя их в соответствие с желаемыми настройками приложения:
    ```dotenv
    ADMIN_EMAIL="admin@example.com" # Замените на свой адрес или поставьте заглушку
    ADMIN_NAME="Admin" #Замените на свое имя или оставьте как есть
    ALLOWED_HOSTS="web liaksej-tiny-cloud-backend localhost 127.0.0.1 [::1] 80" # Добавьте имя хоста вашего сервера.
    CORS_ALLOWED_ORIGINS="http://localhost:3000 http://0.0.0.0:3000 http://web http://nextjs" # Добавьте имя хоста вашего сервера.
    CSRF_TRUSTED_ORIGINS="" # Добавьте имя хоста вашего сервера.
    DATABASE="postgres"   # !!!Не менять
    DATABASE_NAME="liaksej-tiny-cloud-db"
    DATABASE_HOST="db" #!!! Не менять
    DATABASE_PORT=5432
    DATABASE_USER="postgres" # Измените имя пользователя БД, если необходимо.
    DATABASE_PASSWORD="verystrongpassword123" #Установите пароль пользователя БД.
    DEBUG=0
    EMAIL_HOST="smtp.example.com" #Установите smtp-сервер вашей машины или поставьте заглушку.
    EMAIL_HOST_USER="admin@example.com" # Укажите имя администратора или поставьте заглушку.
    EMAIL_HOST_PASSWORD="password" #Укажите пароль от smpt-сервера.
    EMAIL_PORT="588" # Укажите порт smtp-сервера
    EMAIL_USE_TLS="True"
    MEDIA_URL="/media/"
    SECRET_KEY="verystrongsicret123" # Установите secret-key для Django: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
    SIGNING_KEY_JWT="verystrongsicretHS256" #Установите JWT-ключ: python -c "import os; print(os.urandom(32))"
    STATIC_URL="/static/"
    ```
2. Поменяйте имя файла с `.example.env` на `.env`
3. В этой же директории отредактируйте файл `.example.env.db`. Он отвечает за переменные окружения базы данных postgres.
   ```dotenv
   POSTGRES_USER="postgres" # Имя пользователя должно совпадать с именем пользователя в файле .env
   POSTGRES_PASSWORD="verystrongpassword123" # Пароль должен совпадать с паролем пользователя в .env
   POSTGRES_DB="liaksej-tiny-cloud-db" # Название БД должно совпадать с названием БД в .env
   ```   
4. Поменяйте имя файла с `.example.env.db` на `.env.db`
5. В папке `./nginx`, расположенной в коре проекта `liaksej-tiny-cloud-backend`, откройте файл `nginx.conf`.
   Замените `server_name` на имя вашего хоста:
   ```nginx configuration
   # ...
   server {

    listen 80;
    server_name http://yourdomain.name; # укажите имя хоста сервера
   
   # ...
   ```
6. Перейдите в папку склонированного репозитория `liaksej-tiny-cloud-frontend`, откройте
   файл `.example.env.production` и внесите изменения в переменные окружения, установив требуемые значения.
   ```dotenv
   AUTH_SECRET="supersecretkey123" # Устаовите токен для подписи jwt для authjs `openssl rand -base64 32`
   NEXTAUTH_URL="http://yourhostname.com/" # Укажите имя вашего хоста.
   NEXTAUTH_BACKEND_URL="http://web:8000/api/"
   NEXT_PUBLIC_BACKEND_URL="http://web:8000/api/"
   NEXT_PUBLIC_HOSTNAME="http://yourhostname.com/" # Укажите имя вашего хоста.
   ```
7. Поменяйте имя файла с `.example.env.production` на `.env.production`.
8. Откройте файл `Dockerfile` в корне `liaksej-tiny-cloud-frontend`. На 26 строке замените `http://localhost:1337/` на
    имя вашего хоста.
   ```dockerfile
   # ...
   # Замените http://localhost:1337/ на имя вашего хоста.
   ENV NEXT_PUBLIC_HOSTNAME "http://localhost:1337/"
   # ...
   ```

##### Cборка приложения:
1. Вернитесь в каталог `liaksej-tiny-cloud-backen`. Вы готовы к запуску сборки проекта на сервере.
2. Находясь в каталоге `liaksej-tiny-cloud-backen`, запустите сборку приложения через командную строку:
   ```shell
   # Возможно, понадобятся права sudo    
   docker-compose up -d
   ```
   
##### Запуск приложения:
1. После сборки проекта выполните следующие команды для применения миграций, сборке статики для Django и созданию суперпользователя:

   ```shell
   # Для каждой из команд могут потребоваться права sudo
   
   # 1. Применяем миграции:    
   docker-compose exec web python manage.py migrate --noinput
   
   # 2. Собираем статику:
   docker-compose exec web python manage.py collectstatic --noinput 
   
   # 3. Создаем суперпользователя:
   docker-compose exec web python manage.py createsuperuser
   ```

   _Важные комментарии_ 
   > Суперпользователь, которого мы создали, может войти в пользовательский интерфейс приложения, но не может загружать файлы.
   > Поэтому его следует использовать исключительно как `root`-пользователя - для административной панели django `/api/admin`.
   > 
   > Для администрирования пользовательского интерфейса пройдите регистрацию в приложении `/signup`, а затем через 
   > первого суперпользователя выдайте права администратора зарегистрированному пользователю в административной панели Django 
   > `/api/admin`. Таким образом зарегистрированный и получивший права администратора пользователь сможет выполнять все действия
   > администратора через административную панель пользовательского интерфейса, а также загружать файлы в собственное хранилище.

2. Откройте браузер и перейдите на главную страницу вашего хоста. Если вы все сделали правильно, откроется
   главная страница приложения. 
3. Пройдите процесс регистрации и получите права администратора, как указано в примечании выше.








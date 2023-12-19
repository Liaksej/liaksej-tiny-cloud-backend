# Tiny Cloud

Веб-приложение для безопасного облачного хранения файлов.

---

## Структура приложения

Приложение состоит из двух частей: backend и frontend. Каждая часть помещена в отдельный репозиторий. 

### Структура frontend ([liaksej-tiny-cloud-frontend](https://github.com/Liaksej/liaksej-tiny-cloud-frontend))

Пользовательская часть приложения написана на TypeScript  b реализована на фреймворке [Nextjs 14.0.3](https://nextjs.org/docs) с App Router.

Помимо [Nextjs](https://nextjs.org/docs) для создания пользовательской части приложения использованы следующие технологии:
- [React](https://react.dev);
- [tailwindcss](https://tailwindcss.com/docs);
- [Auth.js](https://authjs.dev) aka NextAuth.js - гибкое и безопасное решение для аутентификации веб приложений;
- [clsx](https://github.com/lukeed/clsx) - маленькая утилита для создания условий в строке className;
- [zod](https://zod.dev) - проверка схемы TypeScript с помощью статического вывода типов;
- [use-debounce](https://github.com/xnimorz/use-debounce) - реакт-хук для debounce поиска;
- [sharp](https://github.com/lovell/sharp) - прилжоение для конвертации картинок в меньшие форматы для standalone сборки Nextjs;
- [cypress](https://www.cypress.io) - приложение для E2E тестирования;
- [pnpm](https://pnpm.io) - пакетный менеджер;
- [docker](https://docs.docker.com)

Корневой каталог приложения состоит из следующих файлов и директорий:

[Каталог cypress](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/cypress) содержит тесты и настройки для E2E тестирования прилжоения:

- [каталог e2e](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/cypress/e2e) содержит тесты
- [каталог fixtures](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/cypress/fixtures) содержит предустановленные фикстуры к тестам
- [каталог integration](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/cypress/integration) содержит скрипты для аутентификации
- [каталог support](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/cypress/support) содержит вспомогательные команды и другие полезные утилиты для работы cypress.

_Важный момент:_
> Cypress не совсем корректно работает с Typescript 5.2 и выше, на котором написано приложение и который используется в настройках
> Nextjs. Эта проблема описана в [документации](https://nextjs.org/docs/app/building-your-application/testing/cypress). 
> Для успешного запуска тестов необходимо:
> 1. В файле [tsconfig.json](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/tsconfig.json) заменить "moduleResolution": "bundler" на "moduleResolution": "node" на время тестов.
> 2. Иметь настроенное и запущенное приложение (клиент и сервер);
> 3. Иметь суперпользователя с электронной почтой admin@example.com и паролем 45641231.
> 4. Команда для запуска `pnpm run cypress:run`
> 
> Не забудьте вернуть "bundler" в [tsconfig.json](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/tsconfig.json) после выполнения тестов.

[Каталог public](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/public) содержит статические файлы (картинки) для UI приложения.

Файл hero-desktop.png используется на основании [лицензионного соглашения ](https://pixabay.com/service/license-summary/)

[Каталог src](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src) является основным каталогом приложения, в котором хранится вся его кодовая база:

Каталог разбит на следующие подкаталоги:

 [app](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/app) - каталог представляет собой [роутер приложения](https://nextjs.org/docs/app/building-your-application/routing).
 - ветка `admin` - роут на панель администратора пользовательского интерфейса, содержит:
   - файл `page.tsx` - страница панели администратора пользовательского интерфейса;
   - файл `layout.tsx` - лэйаут страницы панели администратора пользовательского интерфейса;
   - файл `error.tsx` - страница-заглушка при возникновении ошибки на панели администратора;
   - ветка `[name]` - роут в пользовательское хранилище из панели администратора. Он состоит из:
     - файл `page.tsx` - страница пользовательского хранилища из панели администратора;
     - файл `error.tsx` - страница-заглушка при возникновении ошибки на панели администратора;
     - ветка `[id]/edit` - роут на страницу редактирования атрибутов файла пользователя из панели администратора;
       - файл `page.tsx` - страница редактирования атрибутов файла пользователя из панели администратора;
       - файл `not_found.tsx` - страница-заглушка на случай перехода на страницу редактирования атрибутов файла пользователя из панели администратора, которая не существует;
 - ветка `dashboard` - роут на главную панель управления личных файловым хранилищем;
   - файл page.tsx - страница панели управления личных файловым хранилищем;
   - файл `layout.tsx` - лэйаут страницы панели управления личных файловым хранилищем;
   - файл `error.tsx` - страница-заглушка при возникновении ошибки на панели администратора;
   - ветка `[id]/edit` - роут на страницу редактирования атрибутов файла пользователя;
     - файл `page.tsx` - страница редактирования атрибутов файла пользователя;
     - файл `not_found.tsx` - страница-заглушка на случай перехода на страницу редактирования атрибутов файла пользователя, которая не существует;
 - ветка `download/[id]` - роут к эндпоинту для скачивания приватного файла пользователя;
   - файл `route.ts` - [route handler](https://nextjs.org/docs/app/building-your-application/routing/route-handlers) для получения приватного файла пользователя, выполняющий процесс аутентификации.
 - ветка `login` - роут на страницу входа в приложение;
   - файл `page.tsx` - страница входа в приложение;
 - ветка signup - роут на страницу регистрации в приложении;
   - файл `page.tsx` - страница регистрации в приложении;
 - файл `page.tsx` - главная страница приложения;
 - файл `layout.tsx` - лэйаут главной страницы приложения с основными настройками шрифтов;
   
 


### Структура backend ([liaksej-tiny-cloud-backend](https://github.com/Liaksej/liaksej-tiny-cloud-backend))

Серверная часть приложения написана на Python3 реализована на фреймворке [Django 5.0](https://docs.djangoproject.com/en/5.0/) cовместно с [Django REST framework](https://www.django-rest-framework.org).

Помимо [Django 5.0](https://docs.djangoproject.com/en/5.0/) и [Django REST framework](https://www.django-rest-framework.org) для создания серверной части приложения использованы следующие технологии:
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) - плагин JWT аутентификации для Django REST Framework;
- [poetry](https://python-poetry.org) - менеджер пакетов для python;
- [pytest](https://docs.pytest.org/en/7.4.x/) - фреймворк для тестирования;
- [beautifulsoup4](https://beautiful-soup-4.readthedocs.io/en/latest/) - библиотеке для парсинга HTML;
- [docker](https://docs.docker.com);
- [docker-compose](https://docs.docker.com/compose/);

---
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

---








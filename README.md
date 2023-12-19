# Tiny Cloud

![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Frepos%2FLiaksej%2Fliaksej-tiny-cloud-frontend%2Ftags&query=%24%5B0%5D%5B'name'%5D&label=version)

**backend-part** -----> frontend-part [here](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main)

Веб-приложение для безопасного облачного хранения файлов. 

_Загружайте, храните, отображайте, отправляйте, скачивайте и переименовывайте ваши файлы._

---

## Структура приложения

Приложение состоит из двух частей: backend и frontend. Каждая часть помещена в отдельный репозиторий. 

### Структура frontend ([liaksej-tiny-cloud-frontend](https://github.com/Liaksej/liaksej-tiny-cloud-frontend))

Пользовательская часть приложения написана на TypeScript и реализована на фреймворке [Nextjs 14](https://nextjs.org/docs) с App Router.

Помимо [Nextjs](https://nextjs.org/docs) для создания пользовательской части приложения использованы следующие технологии:
- [React](https://react.dev);
- [tailwindcss](https://tailwindcss.com/docs);
- [Auth.js](https://authjs.dev) aka NextAuth.js - гибкое и безопасное решение для аутентификации веб приложений;
- [clsx](https://github.com/lukeed/clsx) - маленькая утилита для создания условий в строке className;
- [zod](https://zod.dev) - проверка схемы TypeScript с помощью статического вывода типов;
- [use-debounce](https://github.com/xnimorz/use-debounce) - react-хук для debounce поиска;
- [sharp](https://github.com/lovell/sharp) - приложение для конвертации картинок в меньшие форматы для standalone сборки Nextjs;
- [cypress](https://www.cypress.io) - приложение для E2E тестирования;
- [pnpm](https://pnpm.io) - пакетный менеджер;
- [docker](https://docs.docker.com)

#### Корневой каталог приложения состоит из следующих файлов и директорий:

**[Каталог cypress](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/cypress) содержит тесты и настройки для E2E тестирования приложения:**

- [каталог e2e](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/cypress/e2e) содержит тесты
- [каталог fixtures](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/cypress/fixtures) содержит предустановленные фикстуры к тестам
- [каталог integration](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/cypress/integration) содержит скрипты для аутентификации
- [каталог support](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/cypress/support) содержит вспомогательные команды и другие полезные утилиты для работы cypress.

_Важный момент:_
> Cypress не совсем корректно работает с Typescript 5.2 и выше, на котором написано приложение. Эта проблема описана в [документации](https://nextjs.org/docs/app/building-your-application/testing/cypress). 
> Для успешного запуска тестов необходимо:
> 1. В файле [tsconfig.json](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/tsconfig.json) заменить "moduleResolution": "bundler" на "moduleResolution": "node" на время тестов.
> 2. Иметь настроенное и запущенное приложение (клиент и сервер);
> 3. Иметь суперпользователя с электронной почтой admin@example.com и паролем 45641231.
> 4. Команда для запуска `pnpm run cypress:run`
> 
> Не забудьте вернуть "bundler" в [tsconfig.json](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/tsconfig.json) после выполнения тестов.

**[Каталог public](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/public) содержит статические файлы (картинки) для UI приложения.**

Файл hero-desktop.png используется на основании [лицензионного соглашения ](https://pixabay.com/service/license-summary/)

**[Каталог src](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src) является основным каталогом приложения, в котором хранится вся его кодовая база:**

Каталог разбит на следующие подкаталоги:

 - Каталог [app](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/app) - это [роутер](https://nextjs.org/docs/app/building-your-application/routing) приложения.
   - ветка [`admin`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/app/admin) - роут на панель администратора пользовательского интерфейса, содержит:
     - файл [`page.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/admin/page.tsx) - страница панели администратора пользовательского интерфейса;
     - файл [`layout.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/admin/layout.tsx) - лэйаут страницы панели администратора пользовательского интерфейса;
     - файл [`error.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/admin/error.tsx) - страница-заглушка при возникновении ошибки на панели администратора;
     - ветка [`[name]`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/app/admin/%5Bname%5D) - роут в пользовательское хранилище из панели администратора. Он состоит из:
       - файл [`page.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/admin/%5Bname%5D/page.tsx) - страница пользовательского хранилища из панели администратора;
       - файл [`error.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/admin/%5Bname%5D/error.tsx) - страница-заглушка при возникновении ошибки на панели администратора;
       - ветка [`[id]/edit`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/app/admin/%5Bname%5D/%5Bid%5D/edit) - роут на страницу редактирования атрибутов файла пользователя из панели администратора;
         - файл [`page.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/admin/%5Bname%5D/%5Bid%5D/edit/page.tsx) - страница редактирования атрибутов файла пользователя из панели администратора;
         - файл [`not_found.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/admin/%5Bname%5D/%5Bid%5D/edit/not-found.tsx) - страница-заглушка на случай перехода на страницу редактирования атрибутов файла пользователя из панели администратора, которая не существует;
   - ветка [`dashboard`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/app/dashboard) - роут на главную панель управления личных файловым хранилищем;
     - файл [`page.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/dashboard/page.tsx) - страница панели управления личных файловым хранилищем;
     - файл [`layout.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/dashboard/layout.tsx) - лэйаут страницы панели управления личных файловым хранилищем;
     - файл [`error.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/dashboard/error.tsx) - страница-заглушка при возникновении ошибки на панели администратора;
     - ветка [`[id]/edit`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/app/dashboard/%5Bid%5D/edit) - роут на страницу редактирования атрибутов файла пользователя;
       - файл [`page.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/dashboard/%5Bid%5D/edit/page.tsx) - страница редактирования атрибутов файла пользователя;
       - файл [`not_found.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/dashboard/%5Bid%5D/edit/not-found.tsx) - страница-заглушка на случай перехода на страницу редактирования атрибутов файла пользователя, которая не существует;
   - ветка [`download/[id]`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/app/download/%5Bid%5D) - роут к эндпоинту для скачивания приватного файла пользователя;
     - файл [`route.ts`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/download/%5Bid%5D/route.ts) - [route handler](https://nextjs.org/docs/app/building-your-application/routing/route-handlers) для получения приватного файла пользователя, выполняющий процесс аутентификации.
   - ветка [`login`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/app/login) - роут на страницу входа в приложение;
     - файл [`page.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/login/page.tsx) - страница входа в приложение;
   - ветка [`signup`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/app/signup) - роут на страницу регистрации в приложении;
     - файл [`page.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/signup/page.tsx) - страница регистрации в приложении;
   - файл [`page.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/page.tsx) - главная страница приложения;
   - файл [`layout.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/layout.tsx) - лэйаут главной страницы приложения с основными настройками шрифтов;
   
- Каталог [lib](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/lib) содержит сервисные функции
клиентской части приложения.
  - файл [`actions`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/lib/actions.ts) содержит функции, отвечающие за отправку данных по API, а также изменение этих данных:
    - функция [`authenticate`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/1b59a73ec121f043f9590699ffa9a690478c9b71/src/lib/actions.ts#L10C26-L10C26) отвечает за авторизацию через форму входа;
    - функция [`sendFileToServer`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/1b59a73ec121f043f9590699ffa9a690478c9b71/src/lib/actions.ts#L29C30-L29C30) отвечает за загрузку файлов на сервер;
    - функция [`deleteFile`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/1b59a73ec121f043f9590699ffa9a690478c9b71/src/lib/actions.ts#L62C24-L62C24) отвечает за удаление файла с сервера;
    - функция [`deleteUser`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/1b59a73ec121f043f9590699ffa9a690478c9b71/src/lib/actions.ts#L89C29-L89C29) отвечает за удаление пользователя;
    - функция [`updateFile`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/1b59a73ec121f043f9590699ffa9a690478c9b71/src/lib/actions.ts#L116C26-L116C26) отвечает за внесение изменений в файл;
    - функция [`updateAdminStatus`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/1b59a73ec121f043f9590699ffa9a690478c9b71/src/lib/actions.ts#L155C27-L155C27) отвечает за изменение статуса администратора у пользователя;
    - функция [`registrate`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/1b59a73ec121f043f9590699ffa9a690478c9b71/src/lib/actions.ts#L186C24-L186C24) отвечает за регистрацию пользователя в приложении;
  - файл [`data`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/lib/data.ts) содержит функции, отвечающие за получение данных по API:
    - функция [`fetchDataFromAPI`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/1b59a73ec121f043f9590699ffa9a690478c9b71/src/lib/data.ts#L6C27-L6C27) отвечает за выполнение fetch-запросов;
    - функция [`fetchTableData`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/1b59a73ec121f043f9590699ffa9a690478c9b71/src/lib/data.ts#L39C27-L39C27) отвечает за получение списка файлов / пользователей;
    - функция [`fetchFilesPages`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/1b59a73ec121f043f9590699ffa9a690478c9b71/src/lib/data.ts#L68C26-L68C26) отвечает за получение количества страниц для пагинатора;
    - функция [`fetchFile`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/1b59a73ec121f043f9590699ffa9a690478c9b71/src/lib/data.ts#L92) отвечает за получение данных о конкретном файле;
    - функция [`adminCheck`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/1b59a73ec121f043f9590699ffa9a690478c9b71/src/lib/data.ts#L106) отвечает за дополнительную проверку прав доступа пользователя (если пользователь является администратором, в интерфейсе отображается административная панель);
  - файл [`definitions`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/lib/definitions.ts) содержит описания типов и интерфейсов объектов TypeScript;
  - файл [`utils`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/lib/utils.ts) содержит функции-утилиты для пагинации, обработки отображаемой даты и размера файлов;

- Каталог [ui](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/ui) содержит набор react-компонентов для UI приложения;
  - ветка [`adminPanel`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/ui/adminPanel) содержит компоненты административной панели:
    - компонент [`AdminTable`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/adminPanel/AdminTable.tsx)- таблица административной панели;
    - компонент [`ChangeAdminStatusButton`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/adminPanel/ChangeAdminStatusButton.tsx) - чек-бокс для изменения статуса администратора;
  - ветка [`dashboard`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/ui/dashboard) содержит компоненты панели управления хранилищем пользователя:
    - компонент [`Breadcrumbs`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/dashboard/Breadcrumbs.tsx) - "хлебные крошки", навигатор по вложенным страницам;
    - компонент [`Buttons`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/dashboard/Buttons.tsx) - кнопка удаления файла / пользователя;
    - компонент [`CopyLinkButton`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/dashboard/CopyLinkButton.tsx) - кнопка копирования/перехода по публичной ссылке файла;
    - компонент [`DashboardTable`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/dashboard/DashboardTable.tsx) - таблица панели управления хранилищем пользователя;
    - компонент [`EditFileForm`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/dashboard/EditFileForm.tsx) - форма редактирования данных файла;
    - компонент [`ModalUpload`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/dashboard/ModalUpload.tsx) - оформление модального окна загрузки файла;
    - компоненты из файла [`Pagination`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/dashboard/Pagination.tsx) - элементы пагинации на панели управления хранилищем пользователя и административной панели;
    - компонент [`Search`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/dashboard/Search.tsx) - поле поиска по названию файла на панели управления хранилищем пользователя / имени пользователя на административной панели;
    - компонент [`UpdateInfoButton`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/dashboard/UpdateInfoButton.tsx) - кнопка сохранения изменений в форме редактирования данных файла;
  - ветка [`sideNav`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/ui/sideNav) содержит компоненты боковой панели;
    - компонент [`AdminLink`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/sideNav/AdminLink.tsx) - кнопка доступа к административной панели;
    - компонент [`CloudLogo`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/sideNav/CloudLogo.tsx) - логотип приложения;
    - компонент [`SideNav`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/sideNav/SideNav.tsx) - главное UI боковой панели;
    - компоненты файла [`UploadFile`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/sideNav/UploadFile.tsx) - кнопка загрузки файла на боковой панели, а также содержание модального окна и кнопки модального окна загрузки файла; 
  - компонент [`Button`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/Button.tsx) - оформление кнопок;
  - компонент [`LoginForm`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/LoginForm.tsx) - форма входа в приложение;
  - компонент [`RegistrationForm`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/RegistrationForm.tsx) - форма регистрации в приложении;
  - файл [`fonts`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/fonts.ts) - определяет шрифты, используемые в UI приложения;
  - файл [`global.css`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/global.css) - определяет некоторые глобальные стили приложения, которые не определены для taiwind;
  - компоненты файла [`skeletons`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/skeletons.tsx) - скелетоны для таблиц панели управления хранилищем пользователя / административной панели;

- файл [`auth.config.ts`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/auth.config.ts) определяет конфигурацию аутентификации в пользовательском интерфейсе приложения и взаимодействие с аутентификацией на сервере;
- файл [`middleware.ts`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/middleware.ts) встраивает аутентификацию в middleware приложения, что обеспечивает контроль прав доступа к каждой странице приложения прямо на сервере до отправки страницы пользователю;

Остальные файлы в корне каталога:

- `.example.env.production` - пример настроек переменных окружения для сборки и работы приложения;
- [`.dockerignore`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/.dockerignore) содержит перечень файлов, игнорируемых Docker при сборке;
- [`.eslintrc.json`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/.eslintrc.json) - файл настройки ESLint для Nextjs;
- [`.gitignore`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/.gitignore) содержит перечень файлов, игнорируемых Git;
- [`Dockerfile`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/Dockerfile) содержит команды сборки контейнера приложения;
- [`cypress.config.ts`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/cypress.config.ts) содержит настройки конфигурации для тестового фреймворка Cypress;
- [`next.config.js`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/next.config.js) содержит настройки конфигурации для Nextjs;
- [`package.json`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/package.json) содержит перечень установленных пакетов и настройки конфигурации проекта, скрипты для отладки/тестирования/сборки проекта;
- [`pnpm-lock.yaml`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/pnpm-lock.yaml) содержит сервисную информацию об установленных пакетах для пакетного менеджера pnpm;
- [`postcss.config.js`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/postcss.config.js) содержит настройки конфигурации обработки CSS при сборке;
- [`tailwind.config.ts`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/tailwind.config.ts) содержит настройки конфигурации tailwindcss;
- [`tsconfig.json`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/tsconfig.json) содержит настройки конфигурации для TypeScript;
- [`types.d.ts`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/types.d.ts) содержит уточнения типов для Auth.js, необходимые для обеспечения взаимодействия Auth.js с SimpleJWT.;


### Структура backend ([liaksej-tiny-cloud-backend](https://github.com/Liaksej/liaksej-tiny-cloud-backend))

Серверная часть приложения написана на Python 3 реализована на фреймворке [Django 5.0](https://docs.djangoproject.com/en/5.0/) cовместно с [Django REST framework](https://www.django-rest-framework.org).

Помимо [Django 5.0](https://docs.djangoproject.com/en/5.0/) и [Django REST framework](https://www.django-rest-framework.org) для создания серверной части приложения использованы следующие технологии:
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) - плагин JWT аутентификации для Django REST Framework;
- [poetry](https://python-poetry.org) - менеджер пакетов для python;
- [pytest](https://docs.pytest.org/en/7.4.x/) - фреймворк для тестирования;
- [beautifulsoup4](https://beautiful-soup-4.readthedocs.io/en/latest/) - библиотеке для парсинга HTML;
- [docker](https://docs.docker.com);
- [docker-compose](https://docs.docker.com/compose/);

#### Корневой каталог приложения состоит из следующих файлов и директорий:

**[Каталог authentication](https://github.com/Liaksej/liaksej-tiny-cloud-backend/tree/main/authentication) содержит одноименное приложение сервера Django, отвечающее за аутентификацию и администрирование:**

- ветка [`migrations`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/tree/main/authentication/migrations) содержит модули миграций;
- модуль [`admin.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/authentication/admin.py) содержит настройки отображения элементов приложения authentication на административной панели Django;
- модуль [`apps.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/authentication/admin.py) содержит информацию о приложении authentication для инициализации в [`settings.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/djangoProject/settings.py);
- модуль [`models.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/authentication/models.py) не содержит дополнительной информации;
- модуль [`serializers.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/authentication/serializers.py) содержит:
  - класс [`UserListSerializer`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/authentication/serializers.py#L10), обеспечивает сериализацию данных для эндпоинта `/api/auth/users/`;
  - класс [`CustomRegisterSerializer`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/authentication/serializers.py#L49) обеспечивает сериализацию данных для регистрации пользователя, эндпоинт `/api/auth/register/`;
- модуль [`urls.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/authentication/urls.py) описывает эндпоинты приложения authentication;
- модуль [`views.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/authentication/views.py) описывает следующие DRF-представления приложения authentication:
    - класс-представление [`LoginView`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/authentication/views.py#L32) обеспечивает возможность аутентифицированного в пользовательском интерфейсе приложения администратора на панель администратора Django без необходимости проходить повторную аутентификацию;
    - класс-представление [`UsersViewSet`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/authentication/views.py#L40) обеспечивает представление списка пользователей, данных отдельного пользователя, удаления пользователя для эндпоинта `/api/auth/users`;
    - класс-представление [`CustomRegisterView`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/authentication/views.py#L71) обеспечивает представление регистрации пользователя для эндпоинта `/api/auth/register/`;

**[Каталог cloud](https://github.com/Liaksej/liaksej-tiny-cloud-backend/tree/main/cloud) содержит одноименное приложение сервера Django, отвечающее за работу с хранилищем файлов пользователя:**

- ветка [`migrations`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/tree/main/cloud/migrations) содержит модули миграций;
- модуль [`admin.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/cloud/admin.py) содержит настройки отображения элементов приложения cloud на административной панели Django;
- модуль [`apps.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/cloud/apps.py) содержит информацию о приложении cloud для инициализации в [`settings.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/djangoProject/settings.py);
- модуль [`models.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/cloud/models.py) содержит описание моделей приложения cloud:
  - класс [`User`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/cloud/models.py#L7) описывает модель пользователя;
  - класс [`File`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/cloud/models.py#L46) описывает модель файла;
- модуль [`permissions.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/cloud/permissions.py) содержит дополнительные настройки авторизации:
  - класс [`IsOwner`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/cloud/permissions.py#L4) проверяет наличие прав владельца файла;
  - класс [`IsOwnerOrStaff`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/cloud/permissions.py#L9) проверяет наличие прав владельца файла или администратора;
- модуль [`serializers.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/cloud/serializers.py) содержит сериалайзер:
  - класс [`FilesListSerializer`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/cloud/serializers.py#L8) обеспечивает сериализацию данных для отображений списка файлов или файла, эндпоинт `/api/cloud/files/`;
- модуль [`services.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/cloud/services.py) содержит сервисные функции для сохранения файла на сервер и удаления файла с сервера;
- модуль [`urls.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/cloud/urls.py) описывает эндпоинты приложения cloud;
- модуль [`views.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/cloud/views.py) описывает следующие DRF-представления приложения cloud:
    - класс-представление [`FileViewSet`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/cloud/views.py#L19) обеспечивает представление списка файлов, данных отдельного файла, удаления и изменения файлов для эндпоинта `/api/cloud/files/`;
    - класс-представление [`FileDownloadMixin`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/cloud/views.py#L64C11-L64C11) обеспечивает корректность процесса передачи файла пользователю (владельцу) для эндпоинта `/api/cloud/download/`;
    - класс-представление [`DownloadFileView`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/cloud/views.py#L84C14-L84C14) обеспечивает процесс передачи файла владельцу (владельцу) для эндпоинта `/api/cloud/download/`;
    - класс-представление [`PublicFileDownloadView`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/cloud/views.py#L93) обеспечивает процесс передачи публичного файла пользователю для эндпоинта `/api/cloud/public/`;

**[Каталог djangoProject](https://github.com/Liaksej/liaksej-tiny-cloud-backend/tree/main/djangoProject) содержит основные настройки сервера фреймворка Django:**

- модуль [`asgi.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/djangoProject/asgi.py) - асинхронная веб-спецификация между сервером и приложением;
- модуль [`settings.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/djangoProject/settings.py) содержит основные настройки сервера;
- модуль [`test_settings.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/djangoProject/test_settings.py) содержит корректирующие настройки сервера для тестирования;
- модуль [`urls.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/djangoProject/urls.py) содержит основные эндпоинты сервера;
- модуль [`wsgi.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/djangoProject/wsgi.py) - веб-спецификация между сервером и приложением;

**[Каталог nginx](https://github.com/Liaksej/liaksej-tiny-cloud-backend/tree/main/nginx) содержит настройки Nginx:**

- файл [`Dockerfile`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/nginx/Dockerfile) содержит инструкции по сборке контейнера nginx;
- файл [`nginx.conf`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/nginx/nginx.conf) содержит настройки nginx;

**[Каталог tests](https://github.com/Liaksej/liaksej-tiny-cloud-backend/tree/main/tests) содержит юнит и интеграционные тесты, а также фикстуры и моки для сервера:**

- каталог [`tests_authentication`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/tree/main/tests/tests_authentication) содержит модуль [`test_auth_api.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/tests/tests_authentication/test_auth_api.py) с интеграционными тестами приложения authentication ;
- каталог [`tests_cloud`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/tree/main/tests/tests_cloud) содержит:
  - модуль [`test_cloud_api.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/tests/tests_cloud/test_cloud_api.py) с интеграционными тестами приложения cloud;
  - модуль [`test_services.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/tests/tests_cloud/test_services.py) с юнит-тестами сервисных функций приложения cloud;

**Остальные файлы в корне каталога:**

- [`.coveragerc`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/.coveragerc) содержит настройки для пакета coverage, обеспечивающего проверку покрытия тестами приложения;
- [`.dockerignore`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/.dockerignore) содержит перечень файлов, игнорируемых Docker при сборке;
- [`.example.env`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/.example.env) - пример настроек переменных окружения для сборки и работы сервера Django;
- [`.example.env.db`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/.example.env.db) - пример настроек переменных окружения для сборки и работы базы данных;
-  [`.gitignore`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/.gitignore) - содержит перечень файлов, игнорируемых Git;
- [`Dockerfile`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/Dockerfile) - содержит команды сборки контейнера сервера Django;
- [`docker-compose.yml`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/docker-compose.yml) - содержит настройки для запуска контейнеров приложения;
- [`entrypoint.sh`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/entrypoint.sh) - shell-скрипт, проверяющий запуск базы данных перед стартом контейнера с сервером Django;
- [`manage.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/manage.py) - исполняемый модуль сервера Django;
- [`poetry.lock`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/poetry.lock) - содержит сервисную информацию об установленных пакетах пакетного менеджера Poetry;
- [`pyproject.toml`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/pyproject.toml) - содержит перечень установленных пакетов и настройки конфигурации приложения для пакетного менеджера Poetry;
- [`pytest.ini`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/pytest.ini) - файл настроек для pytest;

---
## Инструкция по установке на сервер

Приложение можно развернуть на сервере, поддерживающем docker.

Для установки понадобится порядка 1,5 Гб свободного дискового пространства для проекта, 
помимо места для установки [docker](https://docs.docker.com/engine/) и [docker-compose](https://docs.docker.com/compose/install/).

### Процесс установки

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
   ENV NEXT_PUBLIC_HOSTNAME "http://localhost/"
   # ...
   ```

##### Сборка приложения:
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








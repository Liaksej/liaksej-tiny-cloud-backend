# Tiny Cloud

![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Frepos%2FLiaksej%2Fliaksej-tiny-cloud-backend%2Ftags&query=%24%5B0%5D%5B'name'%5D&label=version)

**backend-part** -----> frontend-part [here](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main)

Web application for secure cloud file storage. 

_Upload, store, display, send, download and rename your files._

---
#### Topics:

1. [Application structure](https://github.com/Liaksej/liaksej-tiny-cloud-backend#структура-frontend-liaksej-tiny-cloud-frontend)
   - [frontend](https://github.com/Liaksej/liaksej-tiny-cloud-backend#структура-frontend-liaksej-tiny-cloud-frontend)
   - [backend](https://github.com/Liaksej/liaksej-tiny-cloud-backend#структура-backend-liaksej-tiny-cloud-backend)
2. [Deployment instructions](https://github.com/Liaksej/liaksej-tiny-cloud-backend#инструкция-по-установке-на-сервер)

---

## Application structure

The application consists of two parts: backend and frontend. Each part is placed into a separate repository. 

### Frontend ([liaksej-tiny-cloud-frontend](https://github.com/Liaksej/liaksej-tiny-cloud-frontend))

The user side of the application is written in TypeScript and implemented on the [Nextjs 14](https://nextjs.org/docs) framework with App 
Router.

Apart from [Nextjs](https://nextjs.org/docs), the following technologies are used to create the user part of the application:
- [React](https://react.dev);
- [tailwindcss](https://tailwindcss.com/docs);
- [Auth.js](https://authjs.dev) aka NextAuth.js - flexible and secure solution for web application authentication;
- [clsx](https://github.com/lukeed/clsx) - small utility to create conditions in the className string;
- [zod](https://zod.dev) - TypeScript schema validator with static type inference;
- [use-debounce](https://github.com/xnimorz/use-debounce) - react-hook for debounce search;
- [sharp](https://github.com/lovell/sharp) - application for converting images for Next.js standalone builds;
- [cypress](https://www.cypress.io) - E2E testing application;
- [pnpm](https://pnpm.io) - package manager;
- [docker](https://docs.docker.com)

#### The root directory of the application consists of the following files and directories:

**[Cypress directory](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/cypress) contains tests and settings for E2E testing of the application:**

- [e2e directory](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/cypress/e2e) contains tests
- [fixtures directory](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/cypress/fixtures) contains pre-installed fixtures for the tests
- [integration directory](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/cypress/integration) contains scripts for authenticating
- [support directory](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/cypress/support) contains auxiliary commands and other useful cypress utilities.

_Key point:_
> Cypress does not work correctly with Typescript 5.2 and above, in which the application is written. This problem is described in [documentation](https://nextjs.org/docs/app/building-your-application/testing/cypress). 
> To successfully run the tests, you need to:
> 1. In the [tsconfig.json](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/tsconfig.json) file, replace "moduleResolution": "bundler" to "moduleResolution": "node" for the duration of the tests.
> 2. Have an application (client and server) configured and running;
> 3. Have a superuser with email admin@example.com and password 45641231.
> 4. Command to run `pnpm run cypress:run`
> 
> Don't forget to return "bundler" in [tsconfig.json](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/tsconfig.json) after running the tests.

**[Public directory](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/public) contains static files (images) for the application UI.**

The file hero-desktop.png is used based on the [license agreement ](https://pixabay.com/service/license-summary/)

**[Src directory](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src) is the main directory of the application, where all of its code base is stored:**

The src directory is divided into the following subdirectories:

 - The [app](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/app) directory is the [router](https://nextjs.org/docs/app/building-your-application/routing) of the application.
   - directory [`admin`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/app/admin) - rout to the administrator panel of the user interface, contains:
     - file [`page.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/admin/page.tsx) - page of the administrator panel of the user interface;
     - file [`layout.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/admin/layout.tsx) - layout of the user interface administrator panel page;
     - file [`error.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/admin/error.tsx) - error page when an error occurs on the admin panel;
     - directory [`[name]`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/app/admin/%5Bname%5D) - rout to user storage from the administrator panel. It consists of:
       - file [`page.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/admin/%5Bname%5D/page.tsx) - user page from the administrator panel;
       - file [`error.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/admin/%5Bname%5D/error.tsx) - error page when an error occurs on the admin panel;
       - directory [`[id]/edit`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/app/admin/%5Bname%5D/%5Bid%5D/edit) - rout to the user's file attribute editing page from the admin panel;
         - file [`page.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/admin/%5Bname%5D/%5Bid%5D/edit/page.tsx) - page for editing user file attributes from the administrator panel;
         - file [`not_found.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/admin/%5Bname%5D/%5Bid%5D/edit/not-found.tsx) - Not Found page in case you go to the page of editing user file attributes from the admin panel, which does not exist;
   - directory [`dashboard`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/app/dashboard) - rout to the main control panel of the personal file storage;
     - file [`page.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/dashboard/page.tsx) - personal file storage control panel page;
     - file [`layout.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/dashboard/layout.tsx) - layout page of the personal file storage control panel;
     - file [`error.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/dashboard/error.tsx) - error page when an error occurs on the admin panel;
       - directory [`[id]/edit`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/app/dashboard/%5Bid%5D/edit) - rout to the user file attribute editing page;
         - file [`page.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/dashboard/%5Bid%5D/edit/page.tsx) - page for editing user file attributes;
         - file [`not_found.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/dashboard/%5Bid%5D/edit/not-found.tsx) - Not Found page in case you go to the user file attributes editing page that does not exist;
   - directory [`download/[id]`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/app/download/%5Bid%5D) - rout to the endpoint to download the user's private file;
     - file [`route.ts`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/download/%5Bid%5D/route.ts) - [route handler](https://nextjs.org/docs/app/building-your-application/routing/route-handlers) to retrieve the user's private file that performs the authentication process.
   - directory [`login`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/app/login) - rout to the application's login page;
     - file [`page.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/login/page.tsx) - application login page;
   - directory [`signup`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/app/signup) - rout to the application's registration page;
     - file [`page.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/signup/page.tsx) - application registration page;
   - file [`page.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/page.tsx) - main page of the application;
   - file [`layout.tsx`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/app/layout.tsx) - layout of the main page of the application with basic font settings;
   
- The [lib](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/lib) contains service functions
of the client part of the application.
  - file [`actions`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/lib/actions.ts) contains functions responsible for sending data via API, as well as changing this data:
    - function [`authenticate`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/1b59a73ec121f043f9590699ffa9a690478c9b71/src/lib/actions.ts#L10C26-L10C26) is responsible for authorization through the login form;
    - function [`sendFileToServer`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/1b59a73ec121f043f9590699ffa9a690478c9b71/src/lib/actions.ts#L29C30-L29C30) is responsible for uploading files to the server;
    - function [`deleteFile`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/1b59a73ec121f043f9590699ffa9a690478c9b71/src/lib/actions.ts#L62C24-L62C24) is responsible for deleting the file from the server;
    - function [`deleteUser`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/1b59a73ec121f043f9590699ffa9a690478c9b71/src/lib/actions.ts#L89C29-L89C29) is responsible for deleting the user;
    - function [`updateFile`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/1b59a73ec121f043f9590699ffa9a690478c9b71/src/lib/actions.ts#L116C26-L116C26) is responsible for making changes to the file;
    - function [`updateAdminStatus`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/1b59a73ec121f043f9590699ffa9a690478c9b71/src/lib/actions.ts#L155C27-L155C27) is responsible for changing the administrator status of the user;
    - function [`registrate`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/1b59a73ec121f043f9590699ffa9a690478c9b71/src/lib/actions.ts#L186C24-L186C24) is responsible for registering the user in the application;
  - file [`data`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/lib/data.ts) contains functions responsible for obtaining API data:
    - function [`fetchDataFromAPI`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/1b59a73ec121f043f9590699ffa9a690478c9b71/src/lib/data.ts#L6C27-L6C27) is responsible for executing fetch requests;
    - function [`fetchTableData`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/1b59a73ec121f043f9590699ffa9a690478c9b71/src/lib/data.ts#L39C27-L39C27) is responsible for retrieving the list of files / users;
    - function [`fetchFilesPages`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/1b59a73ec121f043f9590699ffa9a690478c9b71/src/lib/data.ts#L68C26-L68C26) is responsible for getting the number of pages for the paginator;
    - function [`fetchFile`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/1b59a73ec121f043f9590699ffa9a690478c9b71/src/lib/data.ts#L92) is responsible for retrieving data about a particular file;
    - function [`adminCheck`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/1b59a73ec121f043f9590699ffa9a690478c9b71/src/lib/data.ts#L106) is responsible for additional checking of user access rights (if the user is an administrator, the administrative panel is displayed in the interface);
  - file [`definitions`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/lib/definitions.ts) contains descriptions of the types and interfaces of TypeScript objects;
  - file [`utils`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/lib/utils.ts) contains utility functions for pagination, handling the displayed date and file size;

- Directory [ui](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/ui) contains a set of React components for the application UI;
  - directory [`adminPanel`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/ui/adminPanel) contains components of the administrative panel:
    - component [`AdminTable`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/adminPanel/AdminTable.tsx) contains administrative panel table;
    - component [`ChangeAdminStatusButton`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/adminPanel/ChangeAdminStatusButton.tsx) contains checkbox to change the administrator status;
  - directory [`dashboard`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/ui/dashboard) contains components of the user storage control panel:
    - component [`Breadcrumbs`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/dashboard/Breadcrumbs.tsx) contains breadcrumbs, navigator to subpages;
    - component [`Buttons`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/dashboard/Buttons.tsx) contains the button to delete a file / user;
    - component [`CopyLinkButton`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/dashboard/CopyLinkButton.tsx) contains the button to copy/pass the public link of the file;
    - component [`DashboardTable`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/dashboard/DashboardTable.tsx) - table of the user's storage control panel;
    - component [`EditFileForm`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/dashboard/EditFileForm.tsx) - file data editing form;
    - component [`ModalUpload`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/dashboard/ModalUpload.tsx) - modal window layout of the file upload window;
    - components from file [`Pagination`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/dashboard/Pagination.tsx) - pagination elements on the user store control panel and administration panel;
    - component [`Search`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/dashboard/Search.tsx) - search field by file name on the user storage control panel / username on the administration panel;
    - component [`UpdateInfoButton`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/dashboard/UpdateInfoButton.tsx) - button to save changes in the file data editing form;
  - ветка [`sideNav`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/tree/main/src/ui/sideNav) contains sidebar components;
    - component [`AdminLink`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/sideNav/AdminLink.tsx) - button to access the administrative panel;
    - component [`CloudLogo`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/sideNav/CloudLogo.tsx) - application logo;
    - component [`SideNav`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/sideNav/SideNav.tsx) - main sidebar UI;
    - components from file [`UploadFile`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/sideNav/UploadFile.tsx) - file upload button in the sidebar, as well as the contents of the modal window and the file upload modal window button; 
  - component [`Button`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/Button.tsx) - buttons UI;
  - component [`LoginForm`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/LoginForm.tsx) - application login form;
  - component [`RegistrationForm`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/RegistrationForm.tsx) - registration form of the application;
  - file [`fonts`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/fonts.ts) defines fonts used in the application's UI;
  - file [`global.css`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/global.css) - defines some global application styles that are not defined for Tailwind CSS;
  - components from file [`skeletons`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/ui/skeletons.tsx) - skeletons for user storage control panel / administration panel tables;

- file [`auth.config.ts`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/auth.config.ts) defines the authentication configuration in the application user interface and the interaction with authentication on the server;
- file [`middleware.ts`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/src/middleware.ts) embeds authentication into the application middleware, which ensures that access rights to each application page are controlled right on the server before the page is sent to the user;

The rest of the files are in the rout of the directory:

- `.example.env.production` - example of environment variable settings for building and running the application;
- [`.dockerignore`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/.dockerignore) contains the list of files ignored by Docker during build;
- [`.eslintrc.json`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/.eslintrc.json) - ESLint customization file for Next.js;
- [`.gitignore`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/.gitignore) contains a list of files ignored by Git;
- [`Dockerfile`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/Dockerfile) contains commands to build the application container;
- [`cypress.config.ts`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/cypress.config.ts) contains configuration settings for Cypress;
- [`next.config.js`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/next.config.js) contains configuration settings for Next.js;
- [`package.json`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/package.json) contains a list of installed packages and project configuration settings, scripts for debugging/testing/building the project;
- [`pnpm-lock.yaml`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/pnpm-lock.yaml) contains service information about installed packages for the pnpm package manager;
- [`postcss.config.js`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/postcss.config.js) contains the configuration settings for CSS processing at build time;
- [`tailwind.config.ts`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/tailwind.config.ts) contains the tailwindcss configuration settings;
- [`tsconfig.json`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/tsconfig.json) contains the configuration settings for TypeScript;
- [`types.d.ts`](https://github.com/Liaksej/liaksej-tiny-cloud-frontend/blob/main/types.d.ts) contains the type refinements for Auth.js needed to enable Auth.js to interoperate with SimpleJWT;


### Backend structure ([liaksej-tiny-cloud-backend](https://github.com/Liaksej/liaksej-tiny-cloud-backend))

The server part of the application is written in Python 3 implemented on the framework [Django 5.0](https://docs.djangoproject.com/en/5.0/) in conjunction with the [Django REST framework](https://www.django-rest-framework.org).

In addition to [Django 5.0](https://docs.djangoproject.com/en/5.0/) and [Django REST framework](https://www.django-rest-framework.org) the following technologies are used to create the server part of the application:
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) - JWT authentication plugin for Django REST Framework;
- [poetry](https://python-poetry.org) - package manager for python;
- [pytest](https://docs.pytest.org/en/7.4.x/) - testing framework;
- [beautifulsoup4](https://beautiful-soup-4.readthedocs.io/en/latest/) - HTML parsing library;
- [docker](https://docs.docker.com);
- [docker-compose](https://docs.docker.com/compose/);

#### The root directory of the application consists of the following files and directories:

**[Application authentication](https://github.com/Liaksej/liaksej-tiny-cloud-backend/tree/main/authentication) responsible for authentication and administration:**

- package [`migrations`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/tree/main/authentication/migrations) contains migration modules;
- module [`admin.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/authentication/admin.py) contains settings for displaying authentication application elements on the Django administration panel;
- module [`apps.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/authentication/admin.py) contains information about the authentication application to be initialized in the [`settings.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/djangoProject/settings.py);
- module [`models.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/authentication/models.py) does not contain any additional information;
- module [`serializers.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/authentication/serializers.py) contains:
  - class [`UserListSerializer`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/authentication/serializers.py#L10), provides data serialization for the `/api/auth/users/` endpoint;
  - class [`CustomRegisterSerializer`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/authentication/serializers.py#L49) provides serialization of data for user registration, endpoint `/api/auth/register/`;
- module [`urls.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/authentication/urls.py) describes the endpoints of the authentication application;
- module [`views.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/authentication/views.py) describes the following DRF representations of the authentication application:
    - class-view [`LoginView`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/authentication/views.py#L32) provides the ability to authenticate in the UI of the admin application to the Django admin panel without having to re-authenticate;
    - class-view [`UsersViewSet`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/authentication/views.py#L40) provides a view of the user list, individual user data, user deletion for the `/api/auth/users` endpoint;
    - class-view [`CustomRegisterView`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/authentication/views.py#L71) provides a user registration view for the `/api/auth/register/` endpoint;

**[Application cloud](https://github.com/Liaksej/liaksej-tiny-cloud-backend/tree/main/cloud) responsible for working with the user's file storage:**

- package [`migrations`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/tree/main/cloud/migrations) contains migration modules;
- module [`admin.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/cloud/admin.py) contains settings for displaying cloud application elements on the Django administration panel;
- module [`apps.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/cloud/apps.py) contains information about the cloud application to initialize in the [`settings.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/djangoProject/settings.py);
- module [`models.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/cloud/models.py) contains a description of the cloud application models:
  - class [`User`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/cloud/models.py#L7) describes the user model;
  - class [`File`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/cloud/models.py#L46) describes the model of the file;
- module [`permissions.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/cloud/permissions.py) contains additional authorization settings:
  - class [`IsOwner`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/cloud/permissions.py#L4) checks if the owner of the file has rights;
  - class [`IsOwnerOrStaff`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/cloud/permissions.py#L9) checks if the file owner or administrator has rights;
- module [`serializers.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/cloud/serializers.py) contains a serializer:
  - class [`FilesListSerializer`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/cloud/serializers.py#L8) provides data serialization for file or file list displays, endpoint `/api/cloud/files/`;
- module [`services.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/cloud/services.py) contains service functions for saving a file to the server and deleting a file from the server;
- module [`urls.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/cloud/urls.py) describes the endpoints of the cloud application;
- module [`views.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/cloud/views.py) describes the following DRF representations of the cloud application:
    - class-view [`FileViewSet`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/cloud/views.py#L19) provides file list view, individual file data, file deletion and file modification for the `/api/cloud/files/` endpoint;
    - class-view [`FileDownloadMixin`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/cloud/views.py#L64C11-L64C11) provides correctness of file transfer process to user (owner) for `/api/cloud/download/` endpoint;
    - class-view [`DownloadFileView`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/cloud/views.py#L84C14-L84C14) provides the file transfer process to the owner(s) for the `/api/cloud/download/` endpoint;
    - class-view [`PublicFileDownloadView`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/31cc0ef15ded13394ff9127d12e0646a3fe68acf/cloud/views.py#L93) provides the process of transferring a public file to the user for the `/api/cloud/public/` endpoint;

**[Package djangoProject](https://github.com/Liaksej/liaksej-tiny-cloud-backend/tree/main/djangoProject) contains the basic server settings of the Django framework:**

- module [`asgi.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/djangoProject/asgi.py) - asynchronous web specification between the server and the application;
- module [`settings.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/djangoProject/settings.py) contains the basic server settings;
- module [`test_settings.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/djangoProject/test_settings.py) contains corrective server settings for testing;
- module [`urls.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/djangoProject/urls.py) contains the main endpoints of the server;
- module [`wsgi.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/djangoProject/wsgi.py) - web specification between the server and the application;

**[Directory nginx](https://github.com/Liaksej/liaksej-tiny-cloud-backend/tree/main/nginx) contains Nginx settings:**

- file [`Dockerfile`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/nginx/Dockerfile) contains instructions for building the Nginx container;
- file [`nginx.conf`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/nginx/nginx.conf) contains Nginx settings;

**[Directory tests](https://github.com/Liaksej/liaksej-tiny-cloud-backend/tree/main/tests) Contains unit and integration tests, as well as fixtures and mocs for the server:**

- directory [`tests_authentication`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/tree/main/tests/tests_authentication) contains module [`test_auth_api.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/tests/tests_authentication/test_auth_api.py) with authentication application integration tests;
- directory [`tests_cloud`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/tree/main/tests/tests_cloud) contains:
  - module [`test_cloud_api.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/tests/tests_cloud/test_cloud_api.py) with cloud application integration tests;
  - module [`test_services.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/tests/tests_cloud/test_services.py) with unit tests of service functions of the cloud application;

**The rest of the files are in the rout of the directory:**

- [`.coveragerc`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/.coveragerc) contains settings for the coverage package that provides test coverage verification for the application;
- [`.dockerignore`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/.dockerignore) contains a list of files ignored by Docker during build;
- [`.example.env`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/.example.env) - example of environment variable settings for building and running Django server;
- [`.example.env.db`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/.example.env.db) - example of environment variable settings for building and running the database;
-  [`.gitignore`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/.gitignore) contains a list of files ignored by Git;
- [`Dockerfile`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/Dockerfile) contains commands to build the Django server container;
- [`docker-compose.yml`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/docker-compose.yml) - contains settings for launching application containers;
- [`entrypoint.sh`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/entrypoint.sh) - shell script that checks for database startup before starting the Django server container;
- [`manage.py`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/manage.py) - Django server executable module;
- [`poetry.lock`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/poetry.lock) contains service information about installed Poetry package manager packages;
- [`pyproject.toml`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/pyproject.toml) contains a list of installed packages and application configuration settings for the Poetry package manager;
- [`pytest.ini`](https://github.com/Liaksej/liaksej-tiny-cloud-backend/blob/main/pytest.ini) - settings file for pytest;

---
## Deployment instructions

The application can be deployed on a server that supports docker.

The installation will require about 1.5 GB of free disk space for the project, 
in addition to the installation space [docker](https://docs.docker.com/engine/) and [docker-compose](https://docs.docker.com/compose/install/).

### Deployment process

##### Software preparation:
1. Install Docker: https://docs.docker.com/engine/
2. Install Docker-compose: https://docs.docker.com/compose/install/
3. Install Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
4. Clone the `main` branches of the project repositories into one folder so that they are at the same level. 
For example, `~/tiny-cloud/liaksej-tiny-cloud-backend` and `~/tiny-cloud/liaksej-tiny-cloud-frontend`.

    ```shell
    git clone -b main https://github.com/Liaksej/liaksej-tiny-cloud-backend.git
    
    git clone -b main https://github.com/Liaksej/liaksej-tiny-cloud-frontend.git
    ```

##### Preparing environment variables:
1. In the `/liaksej-tiny-cloud-backend` directory on the server, open the `.example.env` file. This is the configuration file
   for the Django server. Adjust the necessary lines to match the desired application settings:
    ```dotenv
    ADMIN_EMAIL="admin@example.com" # Replace with your address or place a blanking plate
    ADMIN_NAME="Admin" # Replace with your name or leave it as it is
    ALLOWED_HOSTS="web liaksej-tiny-cloud-backend localhost 127.0.0.1 [::1] 80" # Add the hostname of your server.
    CORS_ALLOWED_ORIGINS="http://localhost:3000 http://0.0.0.0:3000 http://web http://nextjs" # Add the hostname of your server.
    CSRF_TRUSTED_ORIGINS="" # Add the hostname of your server.
    DATABASE="postgres"   # !!!Don't change
    DATABASE_NAME="liaksej-tiny-cloud-db"
    DATABASE_HOST="db" #!!! Don't change
    DATABASE_PORT=5432
    DATABASE_USER="postgres" # Change the database username, if necessary.
    DATABASE_PASSWORD="verystrongpassword123" #Set the database user password.
    DEBUG=0
    EMAIL_HOST="smtp.example.com" #Install your machine's smtp server or put in a stub.
    EMAIL_HOST_USER="admin@example.com" # Set the administrator's name or place a blank.
    EMAIL_HOST_PASSWORD="password" #Set the password for the smpt server.
    EMAIL_PORT="588" # Set the port of the smtp server
    EMAIL_USE_TLS="True"
    MEDIA_URL="/media/"
    SECRET_KEY="verystrongsicret123" # Set the secret key for Django: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
    SIGNING_KEY_JWT="verystrongsicretHS256" #Set the JWT key: python -c "import os; print(os.urandom(32))"
    STATIC_URL="/static/"
    ```
2. Change the file name from `.example.env` to `.env`
3. In the same directory, edit the `.example.env.db` file. It is responsible for the postgres database environment variables.
   ```dotenv
   POSTGRES_USER="postgres" # The username must match the username in the .env file
   POSTGRES_PASSWORD="verystrongpassword123" # Password must match the user password in .env
   POSTGRES_DB="liaksej-tiny-cloud-db" # The database name must match the database name in .env
   ```   
4. Change the file name from `.example.env.db` to `.env.db`
5. In the `./nginx` folder located in the `liaksej-tiny-cloud-backend` project bark, open the `nginx.conf` file.
   Replace `server_name` with your hostname:
   ```nginx configuration
   # ...
   server {

    listen 80;
    server_name http://yourdomain.name; # Set the hostname of the server
   
   # ...
   ```
6. Navigate to the `liaksej-tiny-cloud-frontend` folder of the cloned repository, open the
   file `.example.env.production` and modify the environment variables by setting the required values.
   ```dotenv
   AUTH_SECRET="supersecretkey123" # Set the jwt signature token for authjs `openssl rand -base64 32`
   NEXTAUTH_URL="http://yourhostname.com/" # Set your host name.
   NEXTAUTH_BACKEND_URL="http://web:8000/api/"
   NEXT_PUBLIC_BACKEND_URL="http://web:8000/api/"
   NEXT_PUBLIC_HOSTNAME="http://yourhostname.com/" # Set your host name.
   ```
7. Change the file name from `.example.env.production` to `.env.production`.
8. Open the `Dockerfile` file in the root of `liaksej-tiny-cloud-frontend`. On line 26, replace `http://localhost/` with
    your hostname.
   ```dockerfile
   # ...
   # Replace http://localhost/ with your hostname.
   ENV NEXT_PUBLIC_HOSTNAME "http://localhost/"
   # ...
   ```

##### Application Build:
1. Return to the `liaksej-tiny-cloud-backen` directory. You are ready to start building the project on the server.
2. While in the `liaksej-tiny-cloud-backen` directory, run the application build via the command line:
   ```shell
   # You may need sudo privileges
   docker-compose up -d
   ```
Comments:
> If you have trouble with buildx when building the nextjs container and you understand Docker, you can install buildx 
> following the [instructions](https://github.com/docker/buildx#linux-packages). If you don't have time to figure it out, replace
> in the Dockerfile located in the `liaksej-tiny-cloud-frontend` directory with lines 16 and 33:
> ```dockerfile
> # Replace line 16
> RUN --mount=type=cache,id=pnpm,target=/pnpm/store pnpm install --prod --frozen-lockfile
> # With the line:
> RUN pnpm install --prod --frozen-lockfile
> 
> # Replace line 33
> RUN --mount=type=cache,id=pnpm,target=/pnpm/store pnpm install --frozen-lockfile
> # With the line:
> RUN pnpm install --frozen-lockfile
> ```
> It'll take longer to build. But the result is the same. 
> 
   
##### Launching the app:
1. After building the app, run the following commands to apply migrations, build statics for Django, and create a superuser:

   ```shell
   # Each of the commands may require sudo privileges
   
   # 1. Apply migrations:
   docker-compose exec web python manage.py migrate --noinput
   
   # 2. Collect static:
   docker-compose exec web python manage.py collectstatic --noinput 
   
   # 3. Create a superuser:
   docker-compose exec web python manage.py createsuperuser
   ```

   _Important comments_ 
   > The superuser we created can log into the application's UI, but cannot upload files.
   > Therefore, it should be used exclusively as a `root` user - for the django `/api/admin` administrative panel.
   > 
   > To administer the user interface, log in to the `http://your.host/signup` application and then through the 
   > first superuser, grant admin rights to the registered user in the Django administration panel 
   > `http://your.host`. Thus a registered and authorized administrator user will be able to perform all actions
   > through the administrative panel of the user interface, as well as upload files to their own storage.

2. Open your browser and go to your host's home page. If you have done everything correctly,
   the home page of the application. 
3. Go through the registration process and get administrator rights as mentioned in the note above.









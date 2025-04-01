<<<<<<< HEAD
# ForkTech
=======

# Audio File Upload Service

## Описание проекта

Сервис для загрузки и управления аудиофайлами с возможностью авторизации через Яндекс. Пользователи могут загружать аудиофайлы, давать им пользовательские имена и просматривать список своих файлов.

## Основные возможности

* Авторизация через Яндекс OAuth
* Загрузка аудиофайлов с пользовательскими именами
* Хранение файлов в локальной файловой системе
* Управление пользователями (для администраторов)
* Просмотр информации о загруженных файлах

## Технологии

* **Backend** : FastAPI (асинхронный)
* **База данных** : PostgreSQL 16
* **Аутентификация** : Яндекс OAuth + JWT токены
* **Контейнеризация** : Docker

## Установка и запуск

### Требования

* Docker и Docker Compose
* Python 3.11+

### Настройка окружения

1. Создайте файл** **`.env` в корне проекта на основе** **`.env.example`:

   ```
   API_V1_STR=/api/v1
   PROJECT_NAME=AudioUploadService
   YANDEX_CLIENT_ID=your_yandex_client_id
   YANDEX_CLIENT_SECRET=your_yandex_client_secret
   SQLALCHEMY_DATABASE_URL=postgresql://user:password@db:5432/dbname
   DB_USER=user
   DB_PASSWORD=password
   DB_NAME=dbname
   ```


### Запуск сервиса

```
docker-compose up -d
```

### Создание миграций

```
docker-compose exec web alembic revision --autogenerate -m "first init"  docker-compose run migrations
```

### Применение миграций

```
docker-compose exec web alembic upgrade head
```

Также при каждом перезапуске применяются миграции и существует самописный скрипт


```
docker-compose exec web python migrations
```

## API Endpoints

### Аутентификация

* `POST /auth/yandex` -Аутентификация через Яндекс

### Пользователи

* `GET /users/me` - Получить данные текущего пользователя
* `PATCH /users/me` - Изменить данные пользователя
* `DELETE /users/{user_id}` - Удалить пользователя (только для администраторов)

### Страницы

    `GET /` - Виджет для авторизации через Яндекс

### Аудиофайлы

* `POST /audio/upload` - Загрузить аудиофайл
* `GET /audio` - Получить список файлов пользователя
* `DELETE /audio/{file_id}` - Удалить аудиофайл
>>>>>>> 9f8f01f (first commit)

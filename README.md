# Tron Address Info Microservice

Микросервис для получения информации о кошельках в сети Tron (TRX), включая баланс, bandwidth и energy. Сервис сохраняет историю запросов в БД и предоставляет API для доступа к этим данным.

## 🛠 Технологии

- **FastAPI** - веб-фреймворк
- **SQLAlchemy (async)** - работа с БД
- **PostgreSQL** - основная БД
- **TronPy** - клиент для Tron API
- **Alembic** - миграции БД
- **Pytest** - тестирование
- **Docker** - контейнеризация

## 📁 Структура проекта


```
tron-address-service/
├── backend/
│   ├── alembic/               # Конфигурация Alembic
│   │   └── versions/          # Файлы миграций
│   ├── app/
│   │   ├── core/              # Основные настройки приложения
│   │   ├── db/                # Работа с базой данных
│   │   │   ├── migrations/    # Миграции БД (Alembic)
|   |   |   ├── base.py        # Базовый класс модели
|   |   |   ├── session.py     # Подключение к БД
│   │   │   └── models.py      # Модели SQLAlchemy
│   │   ├── endpoints/         # API endpoints
│   │   ├── services/          # Бизнес-логика
│   │   ├── schemas/           # Pydantic-схемы
│   │   ├── tests/             # Тесты (unit+integration)
│   │   └── main.py            # Точка входа FastAPI
│   ├── alembic.ini            # Конфиг Alembic
│   ├── Dockerfile             # Конфигурация Docker
│   ├── migrate.py             # Скрипт для миграций
│   └── requirements.txt       # Зависимости Python
├── docker-compose.yaml         # Конфигурация Docker Compose
├── .env                       # Переменные окружения
└── README.md                  # Документация
```


## 🚀 Запуск проекта

### 1. Сборка и запуск контейнеров

```bash
docker-compose up --build
```

Сервис будет доступен на `http://localhost:9000`

### 2. Миграции базы данных

Создание новой миграции:

```bash
docker-compose exec app alembic revision --autogenerate -m "Описание изменений"
```

Применение миграций:

```bash
docker-compose exec app alembic upgrade head
```

### 3. Тестирование

Запуск всех тестов:

```bash
docker-compose exec app pytest -v
```

Запуск конкретного теста:

```bash
docker-compose exec app pytest -v tests/test_endpoints.py::test_get_address_info
```

## 📚 API Endpoints

### Получить информацию о кошельке

**POST** `/api/v1/address-info/`

```json
{
  "address": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"
}
```

### Получить историю запросов

**GET** `/api/v1/queries/`
Параметры:

- `page` - номер страницы (default: 1)
- `per_page` - элементов на странице (default: 10)

## 🔧 Настройка окружения

Создайте `.env` файл на основе `.env.example`:

```ini
API_V1_STR=/api/v1
BACKEND_CORS_ORIGINS=[]
PROJECT_NAME=TestForkTech
SQLALCHEMY_DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/dbname
APP_PORT=9000
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=dbname
DB_PORT=5432
DB_HOST=db
TRON_URI=https://api.trongrid.io
TRON_API_KEY=Ваш Api-ключ
```

## 📊 Примеры запросов

1. Получение информации о кошельке:

```bash
curl -X POST "http://localhost:8000/api/v1/address-info/" \
  -H "Content-Type: application/json" \
  -d '{"address":"TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"}'
```

2. Получение истории запросов:

```bash
curl "http://localhost:8000/api/v1/queries/?page=1&per_page=5"
```

## 🧪 Тестирование

Проект включает:

- Юнит-тесты сервисов
- Интеграционные тесты API
- Тесты моделей БД

Для запуска с покрытием:

```bash
docker-compose exec app pytest --cov=app --cov-report=html
```

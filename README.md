# Team Management API

Team Management API - це REST API, створений на базі Django, який дозволяє керувати командами та людьми в цих командах. API забезпечує функціональність CRUD (створення, читання, оновлення, видалення) для команд і людей.

## Зміст

- [Team Management API](#team-management-api)
  - [Зміст](#зміст)
  - [Передумови](#передумови)
  - [Встановлення](#встановлення)
  - [Запуск](#запуск)
  - [Наповнення бази даних тестовими даними](#наповнення-бази-даних-тестовими-даними)
    - [Запуск скрипту для наповнення](#запуск-скрипту-для-наповнення)
  - [API Ендпоінти](#api-ендпоінти)
  - [Приклади запитів](#приклади-запитів)
    - [Створення нової команди](#створення-нової-команди)
    - [Додавання людини до команди](#додавання-людини-до-команди)
    - [Перегляд інформації про команду](#перегляд-інформації-про-команду)
    - [Оновлення інформації про команду](#оновлення-інформації-про-команду)
    - [Видалення людини](#видалення-людини)
    - [Пошук людини за ім'ям](#пошук-людини-за-імям)
    - [Сортування людей за ім'ям](#сортування-людей-за-імям)

## Передумови

-   Python 3.10+
-   PostgreSQL
-   Віртуальне середовище (рекомендується)

## Встановлення

1. Клонуйте репозиторій:

    ```bash
    git clone https://github.com/SHASHA184/team_management
    cd team_management
    ```

2. Створіть віртуальне середовище (необов'язково):

    ```bash
    python -m venv my_venv
    ```

3. Активуйте віртуальне середовище (необов'язково):

    - **Linux/macOS**:

        ```bash
        source my_venv/bin/activate
        ```

    - **Windows**:

        ```bash
        my_venv\Scripts\activate
        ```

4. Встановіть залежності:

    ```bash
    pip install -r requirements.txt
    ```

5. Створіть файл `.env.local` у корені проекту та вкажіть налаштування для підключення до бази даних PostgreSQL:

    ```dotenv
    POSTGRES_USER=your_postgres_user
    POSTGRES_PASSWORD=your_postgres_password
    POSTGRES_HOST=your_postgres_host
    POSTGRES_PORT=your_postgres_port
    POSTGRES_DB=your_postgres_db
    ```

6. Виконайте міграції бази даних:

    ```bash
    python manage.py migrate
    ```



## Запуск

1. Запустіть локальний сервер:

    ```bash
    python manage.py runserver
    ```

2. Перейдіть у вашому браузері до [http://localhost:8000](http://localhost:8000), щоб отримати доступ до API.


## Наповнення бази даних тестовими даними

### Запуск скрипту для наповнення

```bash
python populate_db.py
```

Скрипт додасть кілька команд і людей до бази даних з фіксованими даними.


## API Ендпоінти

| Метод  | Ендпоінт         | Опис                            |
| ------ | ---------------- | ------------------------------- |
| GET    | /api/teams/       | Отримати список всіх команд     |
| POST   | /api/teams/       | Створити нову команду           |
| GET    | /api/team/{id}/   | Отримати інформацію про команду |
| PUT    | /api/team/{id}/   | Оновити інформацію про команду  |
| DELETE | /api/team/{id}/   | Видалити команду                |
| GET    | /api/persons/     | Отримати список всіх людей      |
| POST   | /api/persons/     | Створити нову людину            |
| GET    | /api/person/{id}/ | Отримати інформацію про людину  |
| PUT    | /api/person/{id}/ | Оновити інформацію про людину   |
| DELETE | /api/person/{id}/ | Видалити людину                 |

## Приклади запитів

### Створення нової команди

**Запит:**

```http
POST /api/teams/

```

**Тіло запиту:**

```http

{
    "name": "Команда 1"
}
```

**Відповідь:**

```http

{
    "id": 1,
    "name": "Команда 1"
}
```

### Додавання людини до команди

**Запит:**

```http
POST /api/persons/
```

**Тіло запиту:**

```http

{
    "id": 1,
    "first_name": "Іван",
    "last_name": "Іванов",
    "email": "ivanov@example.com",
    "team": 1
}
```

**Відповідь:**

```http
{
    "id": 1,
    "first_name": "Іван",
    "last_name": "Іванов",
    "email": "ivanov@example.com",
    "team": 1
}
```

### Перегляд інформації про команду

**Запит:**

```http
GET /api/team/1/
```

**Відповідь:**

```http
{
    "id": 1,
    "name": "Команда 1",
    "persons": [
        {
            "id": 1,
            "first_name": "Іван",
            "last_name": "Іванов",
            "email": "ivanov@example.com"
        }
    ]
}
```

### Оновлення інформації про команду

**Запит:**

```http
PUT /api/team/1/
```

**Тіло запиту:**

```http
{
    "name": "Нова команда 1"
    "persons": [
        {
            "id": 1,
            "first_name": "Іван",
            "last_name": "Іванов",
            "email": "ivanov@example.com"      
        }
    ]
}
```

**Відповідь:**

```http
{
    "id": 1,
    "name": "Нова команда 1"
}
```

### Видалення людини

**Запит:**

```http
DELETE /api/person/1/
```

**Відповідь:**

```http

HTTP 204 No Content
```

### Пошук людини за ім'ям

**Запит:**

```http
GET /api/persons/?search=Іван
```

**Відповідь:**

```http
[
    {
        "id": 1,
        "first_name": "Іван",
        "last_name": "Іванов",
        "email": "ivanov@example.com",
        "team": 1
    }
]
```

### Сортування людей за ім'ям

**Запит:**

```http
GET /api/persons/?ordering=first_name
```

**Відповідь:**

```http
[
    {
        "id": 1,
        "first_name": "Андрій",
        "last_name": "Андрійов",
        "email": "andriy.andriyov@example.com",
        "team": 1
    },
    {
        "id": 2,
        "first_name": "Іван",
        "last_name": "Іванов",
        "email": "ivanov@example.com",
        "team": 1
    }
]
```
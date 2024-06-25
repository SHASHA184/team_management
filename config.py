from dotenv import load_dotenv
import os

# Завантаження змінних середовища з файлу .env.local
load_dotenv(".env.local")

# Створення конфігураційних змінних
POSTGRES_USER=os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST=os.getenv('POSTGRES_HOST')
POSTGRES_PORT=os.getenv('POSTGRES_PORT')
POSTGRES_DB=os.getenv('POSTGRES_DB')
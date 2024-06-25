import os
import django

# Налаштування Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'team_management.settings')
django.setup()

from teams.models import Team, Person

# Видалення існуючих даних
Team.objects.all().delete()
Person.objects.all().delete()

# Генерація команд
teams_data = [
    {"name": "Alpha"},
    {"name": "Beta"},
    {"name": "Gamma"},
    {"name": "Delta"},
    {"name": "Epsilon"},
]

teams = []
for team_data in teams_data:
    team = Team.objects.create(**team_data)
    teams.append(team)

# Генерація людей
persons_data = [
    {"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "team": teams[0]},
    {"first_name": "Jane", "last_name": "Smith", "email": "jane.smith@example.com", "team": teams[1]},
    {"first_name": "Michael", "last_name": "Johnson", "email": "michael.johnson@example.com", "team": teams[2]},
    {"first_name": "Emily", "last_name": "Davis", "email": "emily.davis@example.com", "team": teams[3]},
    {"first_name": "Daniel", "last_name": "Brown", "email": "daniel.brown@example.com", "team": teams[4]},
    {"first_name": "Jessica", "last_name": "Williams", "email": "jessica.williams@example.com", "team": teams[0]},
    {"first_name": "David", "last_name": "Miller", "email": "david.miller@example.com", "team": teams[1]},
    {"first_name": "Ashley", "last_name": "Wilson", "email": "ashley.wilson@example.com", "team": teams[2]},
    {"first_name": "James", "last_name": "Moore", "email": "james.moore@example.com", "team": teams[3]},
    {"first_name": "Sophia", "last_name": "Taylor", "email": "sophia.taylor@example.com", "team": teams[4]},
]

for person_data in persons_data:
    Person.objects.create(**person_data)

print("База даних успішно наповнена тестовими даними.")

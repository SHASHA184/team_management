from django.urls import path
from .views import team_list, team_detail, person_list, person_detail

urlpatterns = [
    # URL маршрути для команд
    path('teams/', team_list, name='team-list'), # Список команд (GET, POST)
    path('team/<int:pk>/', team_detail, name='team-detail'), # Деталі команди (GET, PUT, DELETE)

    # URL маршрути для людей
    path('persons/', person_list, name='person-list'), # Список людей (GET, POST)
    path('person/<int:pk>/', person_detail, name='person-detail'), # Деталі людини (GET, PUT, DELETE)
]

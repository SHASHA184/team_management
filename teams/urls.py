from django.urls import path
from . import views

urlpatterns = [
    # URL маршрути для команд
    path('teams/', views.team_list, name='team-list'), # Список команд (GET, POST)
    path('team/<int:pk>/', views.team_detail, name='team-detail'), # Деталі команди (GET, PUT, DELETE)

    # URL маршрути для людей
    path('persons/', views.person_list, name='person-list'), # Список людей (GET, POST)
    path('person/<int:pk>/', views.person_detail, name='person-detail'), # Деталі людини (GET, PUT, DELETE)
]

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Team, Person
from .serializers import TeamSerializer, PersonSerializer, PersonInTeamSerializer
from .filters import TeamFilter, PersonFilter
from django.db import models


@api_view(["GET", "POST"])
def team_list(request):
    """
    Обробляє запити на список команд (GET) та створення нової команди (POST).

    GET: Повертає список всіх команд у форматі JSON. Підтримує фільтрацію за назвою (`name`) та сортування (`ordering`).
         Приклад фільтрації: `/teams/?name=команда`
         Приклад сортування: `/teams/?ordering=name` (за зростанням) або `/teams/?ordering=-name` (за спаданням)
         Приклад пошуку: `/teams/?search=команда`

    POST: Створює нову команду з даними, наданими в запиті.
    """
    if request.method == "GET":
        teams = Team.objects.all()
        team_filter = TeamFilter(request.GET, queryset=teams)
        teams = team_filter.qs  # Отримуємо відфільтрований QuerySet

        search_query = request.GET.get("search", None)
        if search_query:
            teams = teams.filter(name__icontains=search_query)  # Пошук за назвою

        ordering = request.GET.get("ordering", None)
        if ordering:
            teams = teams.order_by(ordering)  # Сортування

        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def team_detail(request, pk):
    """
    Обробляє запити на детальну інформацію про команду (GET), оновлення команди (PUT) та видалення команди (DELETE).

    pk: Первинний ключ команди.
    """
    try:
        team = Team.objects.get(pk=pk)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TeamSerializer(team)
        team_data = serializer.data
        persons = Person.objects.filter(team=team)
        person_serializer = PersonInTeamSerializer(persons, many=True)
        team_data["persons"] = (
            person_serializer.data
        )  # Додавання даних про учасників до відповіді
        return Response(team_data)

    elif request.method == "PUT":
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def person_list(request):
    """
    Обробляє запити на список людей (GET) та створення нової людини (POST).

    GET: Повертає список всіх людей у форматі JSON. Підтримує фільтрацію за ім'ям (`first_name`), прізвищем (`last_name`),
         електронною поштою (`email`) та командою (`team`). Також підтримується пошук за ім'ям, прізвищем та електронною
         поштою (`search`) та сортування (`ordering`).
         Приклад фільтрації: `/persons/?team=1&first_name=Іван`
         Приклад пошуку: `/persons/?search=Іван`
         Приклад сортування: `/persons/?ordering=-email` (за спаданням)

    POST: Створює нову людину з даними, наданими в запиті.
    """
    if request.method == "GET":
        persons = Person.objects.all()
        person_filter = PersonFilter(request.GET, queryset=persons)
        persons = person_filter.qs
        search_query = request.GET.get("search", None)
        if search_query:
            persons = persons.filter(
                models.Q(first_name__icontains=search_query)
                | models.Q(last_name__icontains=search_query)
                | models.Q(email__icontains=search_query)
            )
        ordering = request.GET.get("ordering", None)
        if ordering:
            persons = persons.order_by(ordering)
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def person_detail(request, pk):
    """
    Обробляє запити на детальну інформацію про людину (GET), оновлення людини (PUT) та видалення людини (DELETE).

    pk: Первинний ключ людини.
    """
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

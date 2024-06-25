from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Team, Person
from .serializers import TeamSerializer, PersonSerializer


# CRUD операції для Teams (команди)
@api_view(["GET", "POST"])
def team_list(request):
    if request.method == "GET":
        # Отримання всіх команд
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        # Створення нової команди
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def team_detail(request, pk):
    try:
        # Спроба знайти команду за первинним ключем (pk)
        team = Team.objects.get(pk=pk)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        # Отримання інформації про команду
        serializer = TeamSerializer(team)
        return Response(serializer.data)
    elif request.method == "PUT":
        # Оновлення інформації про команду
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        # Видалення команди
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# CRUD операції для Persons (люди)
@api_view(["GET", "POST"])
def person_list(request):
    if request.method == "GET":
        # Отримання всіх людей
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        # Створення нової людини
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def person_detail(request, pk):
    try:
        # Спроба знайти людину за первинним ключем (pk)
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        # Отримання інформації про людину
        serializer = PersonSerializer(person)
        return Response(serializer.data)
    elif request.method == "PUT":
        # Оновлення інформації про людину
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        # Видалення людини
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

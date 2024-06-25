from rest_framework import serializers
from .models import Team, Person


class TeamSerializer(serializers.ModelSerializer):
    """
    Серіалізатор для моделі Team.

    Мета:
        Визначає, які поля моделі Team будуть включені до серіалізованого представлення.
        У цьому випадку, серіалізатор включає ідентифікатор (id) та назву (name) команди.
    """
    class Meta:
        model = Team
        fields = ["id", "name"]


class PersonSerializer(serializers.ModelSerializer):
    """
    Серіалізатор для моделі Person.

    Мета:
        Визначає, які поля моделі Person будуть включені до серіалізованого представлення.
        У цьому випадку, серіалізатор включає ідентифікатор (id), ім'я (first_name), прізвище (last_name),
        адресу електронної пошти (email) та ідентифікатор команди (team), до якої належить особа.
        Поле team є полем первинного ключа, яке читається, але не може бути змінено через цей серіалізатор.
    """
    team = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Person
        fields = ["id", "first_name", "last_name", "email", "team"]


class PersonInTeamSerializer(serializers.ModelSerializer):
    """
    Серіалізатор для відображення інформації про учасників команди.

    Мета:
        Визначає, які поля моделі Person будуть включені до серіалізованого представлення при відображенні 
        учасників команди. У цьому випадку, серіалізатор включає ідентифікатор (id), ім'я (first_name), 
        прізвище (last_name) та адресу електронної пошти (email) учасника команди.
        Поле team не включається, оскільки воно вже відоме з контексту команди.
    """
    class Meta:
        model = Person
        fields = ["id", "first_name", "last_name", "email"]

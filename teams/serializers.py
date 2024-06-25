from rest_framework import serializers
from .models import Team, Person


class TeamSerializer(serializers.ModelSerializer):
    # Серіалізатор команди містить ID та назву команди
    class Meta:
        model = Team
        fields = ["id", "name"]


class PersonSerializer(serializers.ModelSerializer):
    # Серіалізатор людини містить ID, ім'я, прізвище, email та ID команди
    team = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Person
        fields = ["id", "first_name", "last_name", "email", "team"]


class PersonInTeamSerializer(serializers.ModelSerializer):
    # Серіалізатор для відображення учасників команди
    class Meta:
        model = Person
        fields = ["id", "first_name", "last_name", "email"]

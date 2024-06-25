import django_filters
from .models import Team, Person

class TeamFilter(django_filters.FilterSet):
    """
    Фільтр для моделей Team.
    """
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Team
        fields = ['name']


class PersonFilter(django_filters.FilterSet):
    """
    Фільтр для моделей Person.
    """
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    team = django_filters.NumberFilter()

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'team']

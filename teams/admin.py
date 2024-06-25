from django.contrib import admin
from .models import Team, Person

# Реєстрація моделей Team та Person в адмін-панелі
admin.site.register(Team)
admin.site.register(Person)

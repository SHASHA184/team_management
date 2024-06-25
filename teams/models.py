from django.db import models

class Team(models.Model):
    """
    Представляє команду.

    Атрибути:
        name (CharField): Назва команди (максимальна довжина 100 символів).
    """
    
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Повертає строкове представлення команди (її назву).
        """
        return self.name


class Person(models.Model):
    """
    Представляє особу, яка може належати до команди.

    Атрибути:
        first_name (CharField): Ім'я особи (максимальна довжина 50 символів).
        last_name (CharField): Прізвище особи (максимальна довжина 50 символів).
        email (EmailField): Адреса електронної пошти особи (має бути унікальною).
        team (ForeignKey): Посилання на команду, до якої належить ця особа 
            (або null, якщо вона не входить до жодної команди).
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='members')

    def __str__(self):
        """
        Повертає строкове представлення особи (ім'я та прізвище).
        """
        return f'{self.first_name} {self.last_name}'

from django.db import models


class Vacancy(models.Model):
    title = models.CharField(max_length=255, verbose_name='Вакансия')
    salary = models.IntegerField(null=True, blank=True, verbose_name='оклад')
    description = models.TextField(default='Нет описания', verbose_name='Описание')
    is_relevant = models.BinaryField(default=True, verbose_name='Актуальность')
    email = models.EmailField(verbose_name='Электронная почта')
    contacts = models.CharField(max_length=100, verbose_name='Контакты')
    def __str__(self):
        return self.title

class Company(models.Model):
    name_c = models.CharField(max_length=255, verbose_name='Название компании')
    address_c = models.CharField(max_length=150, verbose_name='Адрес компании')
    employees = models.IntegerField(null=True, blank=True, verbose_name='Количество сотрудников')
    is_hunting = models.BooleanField(default=True, verbose_name='Ищет работников')

def __str__(self):
    return self.name_c
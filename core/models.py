from django.db import models
from worker.models import Worker, User

class Vacancy(models.Model):
    title = models.CharField(max_length=255, verbose_name='Вакансия')
    salary = models.IntegerField(null=True, blank=True, verbose_name='оклад')
    description = models.TextField(default='Нет описания', verbose_name='Описание')
    is_relevant = models.BinaryField(default=True, verbose_name='Актуальность')
    email = models.EmailField(verbose_name='Электронная почта')
    contacts = models.CharField(max_length=100, verbose_name='Контакты')
    viewed_by = models.ManyToManyField(
        to=User,
        blank=True,
    )
    candidat = models.ManyToManyField(
        to=Worker,
        blank=True,
    )
    category = models.ForeignKey(
        to='Category',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        verbose_name='категория'
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансия'
        ordering = ['salary']


class Company(models.Model):
    name_c = models.CharField(max_length=255, verbose_name='Название компании')
    address_c = models.CharField(max_length=150, verbose_name='Адрес компании')
    employees = models.IntegerField(null=True, blank=True, verbose_name='Количество сотрудников')
    is_hunting = models.BooleanField(default=True, verbose_name='Ищет работников')

def __str__(self):
    return self.name_c


class Category(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

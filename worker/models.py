from django.db import models

class Worker(models.Model):
    name_w = models.CharField(max_length=100, verbose_name='ФИО')
    specialization = models.TextField(max_length=255, verbose_name='специалность')
    salary = models.IntegerField(null=True, blank=True, verbose_name='оклад')
    is_searching = models.BooleanField(default=True, verbose_name='ищет работу')

    def __str__(self):
        return self.name_w

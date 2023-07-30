from django.db import models
from django.contrib.auth.models import User


class Worker(models.Model):
    user = models.OneToOneField(
        to=User,
        null=True,
        blank=False,
        on_delete=models.CASCADE # еще есть и SET_NULL
    )
    name_w = models.CharField(max_length=100, verbose_name='ФИО')
    specialization = models.TextField(max_length=255, verbose_name='специалность')
    w_salary = models.IntegerField(null=True, blank=True, verbose_name='оклад')
    is_searching = models.BooleanField(default=True, verbose_name='ищет работу')

    def __str__(self):
        return self.name_w

class Comment(models.Model):

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    worker = models.ForeignKey(
        to=Worker,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.author.username


class Resume(models.Model):
    text = models.CharField(max_length=255)
    summary = models.TextField()
    skills = models.CharField(max_length=100)
    worker = models.ForeignKey(
        to=Worker,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_photo = models.ImageField(
        null=True, blank=True,
        upload_to="profile_photo/",
        verbose_name="Фото сотрудника"
    )

    def __str__(self):
        return self.text




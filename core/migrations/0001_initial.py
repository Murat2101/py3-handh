# Generated by Django 4.2.2 on 2023-07-14 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('worker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Вакансия')),
                ('salary', models.IntegerField(blank=True, null=True, verbose_name='оклад')),
                ('description', models.TextField(default='Нет описания', verbose_name='Описание')),
                ('is_relevant', models.BooleanField(default=True, verbose_name='Актуальность')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('contacts', models.CharField(max_length=100, verbose_name='Контакты')),
                ('candidates', models.ManyToManyField(blank=True, to='worker.worker')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.category', verbose_name='категория')),
                ('viewed_by', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансия',
                'ordering': ['salary'],
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_c', models.CharField(max_length=255, verbose_name='Название компании')),
                ('address_c', models.CharField(max_length=150, verbose_name='Адрес компании')),
                ('employees', models.IntegerField(blank=True, null=True, verbose_name='Количество сотрудников')),
                ('date_founded', models.DateField(verbose_name='Дата основание')),
                ('is_hunting', models.BooleanField(default=True, verbose_name='Ищет работников')),
                ('workers', models.ManyToManyField(blank=True, related_name='company', to='worker.worker')),
            ],
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-23 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_w', models.CharField(max_length=100, verbose_name='ФИО')),
                ('specialization', models.TextField(max_length=255, verbose_name='специалность')),
                ('salary', models.IntegerField(blank=True, null=True, verbose_name='оклад')),
                ('is_searching', models.BooleanField(default=True, verbose_name='ищет работу')),
            ],
        ),
    ]

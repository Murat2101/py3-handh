# Generated by Django 4.2.2 on 2023-09-07 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recruit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruiter',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='recruit', to=settings.AUTH_USER_MODEL),
        ),
    ]
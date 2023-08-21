from django.db import models
from django.contrib.auth.models import User


class ArticleNew(models.Model):
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=55)
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=True)
    likes_users = models.ManyToManyField(User, blank=True, related_name='like')

    def increase_views_count(self):
        self.views_count += 1
        self.save()



# Create your models here.

from django.urls import path
from .views import *

urlpatterns = [
    path('news/', news_list, name='news-list'),
    path('create/', ArticleNewCreateView.as_view(), name='create-news'),
    path('update/<int:pk>/', ArticleNewCreateView.as_view(), name='update-news'),
    path('<int:id>/', news_detail),
    path('<int:id>/', news_likes),
]
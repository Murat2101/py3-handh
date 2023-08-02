from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .models import ArticleNew





def news_list (request):
    temp = ArticleNew.objects.order_by('-date_added')
    context = {'news': temp}
    return render(request, 'news/news-list.html', context)


class ArticleNewCreateView(CreateView):
    model = ArticleNew
    fields = '__all__'


class ArticleNewUpdateView(UpdateView):
    template = "news/update.html"

# Create your views here.

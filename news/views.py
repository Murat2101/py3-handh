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
def news_detail(request, id):
    new = ArticleNew.objects.get(id=id)
    new.views_count += 1
    new.save()
    return render(request, 'news/new_detail.html', {'new': new})


def news_likes(request, id):
    like = ArticleNew.objects.get(id=id)
    like.likes_users += 1
    like.save()
    return render(request, 'news/likes_detail.html', {'like': like})
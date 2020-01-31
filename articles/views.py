from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    context = {
        'articles':articles
    }
    return render(request,'articles/article_list.html',context)

def article_detail(request,slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    context = {
        'article':article,
    }
    return render(request,'articles/article_detail.html',context)
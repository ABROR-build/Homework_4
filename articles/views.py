from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ArticleForm


def list_topics(request):
    topics = Topics.objects.all()
    context = {
        'topics': topics
    }
    return render(request, 'list_topics.html', context=context)


def list_headlines(request, pk):
    headlines = News.objects.filter(topic_name=pk)
    context = {
        'headlines': headlines
    }
    return render(request, 'list_headlines.html', context=context)


def details(request, pk):
    article = News.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'details.html', context=context)


def add_article(request):
    form = ArticleForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('list_topics')
    context = {
        'form': form
    }
    return render(request, 'new_article.html', context=context)


def edit_article(request, pk):
    obj = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('list_topics')
    else:
        form = ArticleForm(instance=obj)

    context = {
        'form': form
    }
    return render(request, 'edit.html', context)


def delete_article(request, pk):
    obj = get_object_or_404(News, pk=pk)
    if request.method == 'POST' or 'GET':
        obj.delete()
        return render(request, 'delete.html')

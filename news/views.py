from django.http import Http404
from django.shortcuts import get_object_or_404, render
from news.models import News


def home(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context)


def details(request, id):
    try:
        news = get_object_or_404(News, id=id)
        context = {"news": news}
        return render(request, "news_details.html", context)
    except Http404:
        return render(request, "404.html")

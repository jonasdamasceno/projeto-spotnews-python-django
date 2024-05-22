from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from news.forms import CreateCategoryForm
from news.models import News, Category


def home(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context)


def details(request, news_id):
    try:
        news = get_object_or_404(News, id=news_id)
        context = {"news": news}
        return render(request, "news_details.html", context)
    except Http404:
        return render(request, "404.html")


def categories(request):
    form = CreateCategoryForm()
    if request.method == "POST":
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect("home-page")

    context = {"form": form}
    return render(request, "categories_form.html", context)

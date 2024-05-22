from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from news.forms import CreateCategoryForm, CreateNewsModelForm
from news.models import News, Category, User
from rest_framework import viewsets
from news.serializers import CategorySerializer, UserSerializer, NewsSerializer


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


def news(request):
    form = CreateNewsModelForm()

    if request.method == "POST":
        form = CreateNewsModelForm(request.POST, request.FILES)
        if form.is_valid():
            news_instance = form.save(commit=False)
            news_instance.save()
            form.save_m2m()
            return redirect("home-page")

    context = {"form": form}
    return render(request, "news_form.html", context)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

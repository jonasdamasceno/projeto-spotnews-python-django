from django.urls import path
from news.views import home, details, categories, news

urlpatterns = [
    path("", home, name="home-page"),
    path("news/<int:news_id>", details, name="news-details-page"),
    path("categories/", categories, name="categories-form"),
    path("news/", news, name="news-form"),
]

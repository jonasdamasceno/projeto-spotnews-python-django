from django.urls import path
from news.views import home, details

urlpatterns = [
    path("", home, name="home-page"),
    path("news/<int:id>", details, name="news-details-page"),
]

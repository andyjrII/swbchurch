from django.urls import path
from . import views

urlpatterns = [
    path("sermons-search/", views.sermon_list, name="sermonslist"),
    path("sermons/", views.sermons, name="sermons"),
    path("newsevents/details/<int:id>", views.details, name="details"),
    path("newsevents/", views.newsevents, name="newsevents"),
    path("", views.index, name="index"),
]

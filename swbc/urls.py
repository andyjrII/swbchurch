from django.urls import path
from . import views

urlpatterns = [
    path("devotionals/details/<int:id>", views.devotional_details, name="details"),
    path("devotionals/", views.devotionals, name="devotionals"),
    path("sermons/", views.sermons, name="sermons"),
    path("newsevents/details/<int:id>", views.newsevent_details, name="details"),
    path("newsevents/", views.newsevents, name="newsevents"),
    path("", views.index, name="index"),
]

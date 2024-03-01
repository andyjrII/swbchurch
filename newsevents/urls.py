from django.urls import path
from . import views

urlpatterns = [
    path("details/<int:id>", views.newsevent_details, name="details"),
    path("", views.newsevents, name="newsevents"),
]

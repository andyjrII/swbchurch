from django.urls import path
from . import views

urlpatterns = [
    path("", views.devotionals, name="devotionals"),
    path("details/<int:id>", views.devotional_details, name="details"),
]

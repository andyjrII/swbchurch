from django.urls import path
from . import views

urlpatterns = [
    path("", views.sermons, name="sermons"),
]

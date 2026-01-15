from django.urls import path
from . import views

urlpatterns = [
    path("", views.sermons, name="sermons"),
    path("download/<int:sermon_id>/", views.download_sermon, name="download_sermon"),
]

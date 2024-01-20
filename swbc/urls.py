from django.urls import path
from . import views

urlpatterns = [
    path('testing/', views.testing, name='testing'),
    path('', views.index, name='index')
]
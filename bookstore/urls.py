from django.urls import path
from . import views

urlpatterns = [
    path("", views.bookstore, name="bookstore"),
    path("handle_payment_success/", views.handle_payment_success, name="handle_payment_success"),
]

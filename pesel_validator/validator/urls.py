from django.urls import path
from . import views

urlpatterns = [
    path("", views.pesel_validation_view, name="pesel_validator"),
]
from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("wiki", views.index, name="index"),
    path("get", views.get, name="get")
]

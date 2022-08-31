from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("wiki", views.index, name="index"),
    path("css", views.html, name="css"),
    path("django", views.html, name="django"),
    path("git", views.html, name="git"),
    path("html", views.html, name="html"),
    path("python", views.html, name="python"),
    
]

from django.shortcuts import render
from django.urls import path

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
        
    })

def css(request):
    return render(request, "entries/CSS.md")

def django(request):
    return render(request, "entries/Django.md")

def git(request):
    return render(request, "entries/Git.md")

def html(request):
    return render(request, "entries/HTML.md")

def python(request):
    return render(request, "entries/Python.md")
        
    






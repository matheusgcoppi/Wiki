from django.shortcuts import render
from django.urls import path

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
        
    })

def language(request):
    return render(request, "encyclopedia/index.html"), {
        "save": save_entry()
    }


        
    






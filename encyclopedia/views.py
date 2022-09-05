from django.shortcuts import render
from django.urls import path

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()  
    })

def get(request):
    return render(request, "encyclopedia/index.html", {
        "get": util.get_entries()  
    })




        
    






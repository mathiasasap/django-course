from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        "title": "Welcome to my first app!"
    }
    return render(request, 'first_app/index.html', context=context)
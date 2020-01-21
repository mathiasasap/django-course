from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord


def index(request):
    webpages_list = AccessRecord.objects.order_by("date")
    context = {
        "title": "Welcome to my first app!",
        "access_records": webpages_list,
    }
    return render(request, 'first_app/index.html', context=context)
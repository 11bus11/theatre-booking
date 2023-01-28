from django.shortcuts import render
from django.views import generic, View
from django.db import models
from booking.models import Play

from django.contrib import messages

# Create your views here.

def home_page(request):
    plays = Play.objects.all()

    template = "home/index.html"
    context = {
            'plays': plays,
        }

    return render(request, template, context)

    
def about_page(request):
    """ Page with information about the theatre """
    template = "home/about.html"

    return render(request, template)


def success_page(request):
    """ For showing the user their acction succeded (for example when adding a play) """
    template = "home/success.html"

    return render(request, template)
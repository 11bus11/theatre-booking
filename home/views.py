from django.shortcuts import render
from django.views import generic, View
from django.db import models
from booking.models import Play

# Create your views here.

def HomePage(request):
    plays = Play.objects.all()

    template = "home/index.html"
    context = {
            'plays': plays,
        }

    return render(request, template, context)

    
class AboutPage(generic.ListView):
    template_name = "about.html"

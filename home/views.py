from django.shortcuts import render
from django.db import models
from booking.models import Play

# Create your views here.

def HomePage(request):
    model = Play
    plays = Play.objects.all()

    template = "home/index.html"
    context = {
            'plays': plays,
        }

    return render(request, template, context)

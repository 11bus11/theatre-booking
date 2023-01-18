from django.shortcuts import render
from django.db import models
from booking.models import Play

# Create your views here.

def HomePage(request):
    model = Play
    queryset = Play.objects.all()

    template = "home/index.html"

    return render(request, template)

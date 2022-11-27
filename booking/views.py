from django.shortcuts import render
from django.views import generic
from .models import Booking
from .models import NowPlaying

class PlayList(generic.ListView):
    model = NowPlaying
    queryset = 
    template_name = "plays.html"

class Booking(generic.ListView):
    model = Booking
    queryset = 
    template_name = "user.html"


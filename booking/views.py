from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Booking
from .models import NowPlaying



class PlayList(generic.ListView):
    model = NowPlaying
    queryset = NowPlaying.objects.all()
    template_name = "index.html"

class Booking(generic.ListView):
    model = Booking
    queryset =NowPlaying.objects.all()
    template_name = "user.html"


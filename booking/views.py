from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Booking, NowPlaying, Play


def NowPlaying(request):
    model_play = Play
    model_nowplaying = NowPlaying

    template = "booking/play_booking.html"
    
    context = {
        'model_play': model_play,
        'model_nowplaying': model_nowplaying,
    }

    return render(request, template, context)


#def AboutTheatre(request):
#    model = NowPlaying
#    queryset = NowPlaying.objects.all()
#    template_name = "about.html"

def Booking(request):
    model = Booking
    template_name = "user.html"


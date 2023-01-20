from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Booking, NowPlaying, Play


def play_showings(request):
    plays = Play.objects.all()
    showings = NowPlaying.objects.all()

    template = "booking/plays.html"
    context = {
        'plays': plays,
        'showings': showings,
    }

    return render(request, template, context)

def play_dates(request, plays_id):
    play_instance = get_object_or_404(Plays, pk=plays_id)
    showings = NowPlaying.objects.all()

    url = "booking/plays.html"

    context = {
        'play_instance': play_instance,
        'showings': showings,
    }

    return redirect(url)

#def Booking(request):
#    model = Booking
#    template_name = "user.html"


from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Booking, NowPlaying, Play
from .forms import PlayForm, NowPlayingForm, BookingForm


def plays(request):
    plays = Play.objects.all()

    template = "booking/play_booking.html"
    context = {
        'plays': plays,
    }

    return render(request, template, context)

def play_dates(request, play_id):
    play_instance = get_object_or_404(Play, pk=play_id)
    showings = NowPlaying.objects.all()

    template = "booking/date_booking.html"

    context = {
        'play_instance': play_instance,
        'showings': showings,
    }

    return render(request, template, context)

def Booking(request, nowplaying_id):
    showing_instance = get_object_or_404(NowPlaying, pk=nowplaying_id)
    booking_form = BookingForm()

    if request.method == 'POST':
        
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking_form.play = showing_instance.play
            booking_form.viewing = showing_instance.date
            booking_form.save()
            return redirect(reverse('home'))
        else:
            print("error")
    
    template = "booking/form_booking.html"
    context = {
        'showing_instance': showing_instance,
        'booking_form': booking_form
    }

    return render(request, template, context)

@login_required
def add_play(request):
    """ Add a play to the store """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PlayForm(request.POST, request.FILES)
        if form.is_valid():
            play = form.save()
            return redirect(reverse('home'))
        else:
            print("error")
    else:
        form = PlayForm()

    template = 'booking/add_play.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_play(request, play_id):
    """ Edit a play in the store """
    play_instance = get_object_or_404(Play, pk=play_id)
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PlayForm(request.POST, request.FILES, instance=play_instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
        else:
            print("error")
    else:
        form = PlayForm(instance=play_instance)

    template = 'booking/edit_play.html'
    context = {
        'form': form,
        'play_instance': play_instance,
    }

    return render(request, template, context)


@login_required
def delete_play(request, play_id):
    """ Delete a play from the store """
    if not request.user.is_superuser:
        return redirect(reverse('plays'))

    play_instance = get_object_or_404(Play, pk=play_id)
    play_instance.delete()
    print("delete")
    return redirect(reverse('home'))


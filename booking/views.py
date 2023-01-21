from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Booking, NowPlaying, Play
from .forms import PlayForm, NowPlayingForm


def play_showings(request):
    plays = Play.objects.all()
    showings = NowPlaying.objects.all()

    template = "booking/plays.html"
    context = {
        'plays': plays,
        'showings': showings,
    }

    return render(request, template, context)

def play_dates(request, play_id):
    play_instance = get_object_or_404(Play, pk=play_id)
    showings = NowPlaying.objects.all()

    template = "booking/play_booking.html"

    context = {
        'play_instance': play_instance,
        'showings': showings,
    }

    return render(request, template, context)

#def Booking(request):
#    model = Booking
#    template_name = "user.html"

@login_required
def add_play(request):
    """ Add a play to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = playForm(request.POST, request.FILES)
        if form.is_valid():
            play = form.save()
            messages.success(request, 'Successfully added play!')
            return redirect(reverse('play_detail', args=[play.id]))
        else:
            messages.error(request,
                           ('Failed to add play. '
                            'Please ensure the form is valid.'))
    else:
        form = playForm()

    template = 'booking/add_play.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_play(request, play_id):
    """ Edit a play in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    play = get_object_or_404(play, pk=play_id)
    if request.method == 'POST':
        form = playForm(request.POST, request.FILES, instance=play)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated play!')
            return redirect(reverse('play_detail', args=[play.id]))
        else:
            messages.error(request,
                           ('Failed to update play. '
                            'Please ensure the form is valid.'))
    else:
        form = playForm(instance=play)
        messages.info(request, f'You are editing {play.name}')

    template = 'booking/edit_play.html'
    context = {
        'form': form,
        'play': play,
    }

    return render(request, template, context)


@login_required
def delete_play(request, play_id):
    """ Delete a play from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    play = get_object_or_404(play, pk=play_id)
    play.delete()
    messages.success(request, 'play deleted!')
    return redirect(reverse('plays'))


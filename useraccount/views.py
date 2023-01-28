from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    bookings = profile.bookings.all()

    template = 'useraccount/my_account.html'
    context = {
        'bookings': bookings,
        'on_profile_page': True
    }

    return render(request, template, context)
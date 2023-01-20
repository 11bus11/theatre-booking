from django import forms
from useraccount.models import UserProfile
from .models import Play, NowPlaying, Booking


class PlayForm(forms.ModelForm):
    class Meta:
        model_play = Play
        exclude = ()

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'description': 'Description',
            'image': 'Image',
        }


class NowPlayingForm(forms.ModelForm):
    class Meta:
        model = NowPlaying
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'play': 'Play',
            'status': 'Status',
            'seats': 'Seats',
            'date': 'Date',
            'time': 'Time',
        }
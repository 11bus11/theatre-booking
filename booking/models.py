from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "available"), (1, "booked"))


class Play( models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=False, default="To be added")


class NowPlaying(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE )
    status = models.IntegerField(choices=STATUS, default=0)
    seats = models.IntegerField(41)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        ordering = ['status']

class Booking(models.Model):
    playing = models.ForeignKey(NowPlaying, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        ordering = ['-playing']

    def __str__(self):
        return self.name

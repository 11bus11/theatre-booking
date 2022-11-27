from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "available"), (1, "booked"))
PLAYS = ((0, "a christmas carol"), (1, "phantom of the opera"))
DATE = ((0, "10/12"), (1, "13/12"), (2, "17/12"), (3, "20/12"), (4, "23/12"))
TIME = ((0, "12:30"), (1, "16:00"))



class NowPlaying(models.Model):
    play = models.IntegerField(choices=PLAYS)
    status = models.IntegerField(choices=STATUS, default=0)
    seats = models.IntegerField(41)
    date = models.IntegerField(choices=DATE)
    time = models.IntegerField(choices=TIME)

    class Meta:
        ordering = ['status']

class Booking(models.Model):
    play = models.IntegerField(choices=PLAYS)
    time = models.ForeignKey(NowPlaying, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.name

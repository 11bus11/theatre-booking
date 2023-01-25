from django.db import models
from django.contrib.auth.models import User
from useraccount.models import UserProfile

# Create your models here.

STATUS = ((0, "available"), (1, "booked"))


class Play( models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=False, default="To be added")
    image = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class NowPlaying(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)
    seats = models.IntegerField(default=41)
    date = models.DateTimeField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.date)

class Booking(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    viewing = models.ForeignKey(NowPlaying, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    name = models.CharField(max_length=200)
    email = models.EmailField()

    class Meta:
        ordering = ['play']

    def __str__(self):
        return self.name

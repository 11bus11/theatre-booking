from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "available"), (1, "booked"))
PLAYS = ((0, "a christmas carol"), (1, "phantom of the opera"))

class Booking(models.Model):
    play = models.IntegerField(choices=PLAYS)
    date = models.DateField()
    time = models.TimeField()
    name = models.CharField(max_length=200)
    email = models.EmailField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name


class Use(models.Model):
    email = models.EmailField()
    password = models.CharField(min_length=5, max_length=80)

    class Meta:
        ordering = ['email']
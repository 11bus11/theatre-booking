from django.db import models

# Create your models here.

class Play( models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=False, default="To be added")
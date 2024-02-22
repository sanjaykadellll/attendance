from django.db import models

class attandance(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    checkin = models.CharField(max_length=200,blank=True, null=True)
    checkout = models.CharField(max_length=200,blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    post = models.CharField(max_length=200, blank=True, null=True)
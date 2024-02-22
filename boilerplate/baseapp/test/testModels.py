from django.db import models

class test(models.Model):
    firstname1 = models.CharField(max_length=200,blank=True, null=True)
    lastname2 = models.CharField(max_length=100,blank=True, null=True)
    email1 = models.CharField(max_length=200,blank=True, null=True)
    address1 = models.CharField(max_length=200,blank=True, null=True)
    remark1 = models.IntegerField(blank=True, null=True)
	
from django.db import models

class detail(models.Model):
    firstname = models.CharField(max_length=200,blank=True, null=True)
    lastname = models.CharField(max_length=100,blank=True, null=True)
    email = models.CharField(max_length=200,blank=True, null=True)
    address = models.CharField(max_length=200,blank=True, null=True)
    remark = models.IntegerField(blank=True, null=True)
	
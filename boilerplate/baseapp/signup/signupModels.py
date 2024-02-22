from django.db import models

class signup(models.Model):
    name = models.CharField(max_length=200,blank=True, null=True)
    post = models.CharField(max_length=200,blank=True, null=True)
    password = models.CharField(max_length=200,blank=True, null=True)
    confirmpassword = models.CharField(max_length=200,blank=True, null=True)
	
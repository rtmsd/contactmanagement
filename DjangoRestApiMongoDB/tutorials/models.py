from django.db import models


# Create your models here.

class Tutorial(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=70,default='', blank = True, null = True,)
    lastname = models.CharField(max_length=70,default='', blank = True, null = True,)
    gender = models.CharField(max_length=70,default='', blank = True, null = True,)
    emailid = models.EmailField(max_length=70, default='',blank = True, null = True,)
    phoneno = models.CharField(max_length=70,default='', blank = True, null = True,)

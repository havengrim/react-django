from django.db import models

class Member(models.Model):
    fname = models.CharField(max_length=255) 
    lname = models.CharField(max_length=255) 

    email = models.EmailField(max_length=255) 
    passwd = models.CharField(max_length=255) 
    age = models.IntegerField()

    def __str__(self):
        return self.fname + ' ' +  self.lname
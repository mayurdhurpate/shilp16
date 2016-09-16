from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CAUser(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    college = models.CharField(max_length=100)
    year = models.CharField(max_length=15)
    resume = models.CharField(max_length=200)
    promotion = models.TextField(default='Being Shilpified!!')
    def __unicode__(self):
        return "%s, %s, %s" % (self.name, self.college, self.email)


class PPTUser(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    coauthor = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    designation = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __unicode__(self):
        return "%s, %s, %s" % (self.author, self.title, self.college)

    def __str__(self):
        return "%s, %s, %s" % (self.author, self.title, self.college)

class WorkUser(models.Model):
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    designation = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __unicode__(self):
        return "%s, %s" % (self.name, self.college)

    def __str__(self):
        return "%s, %s" % (self.name, self.college)

class greUser(models.Model):
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    designation = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __unicode__(self):
        return "%s, %s" % (self.name, self.college)

    def __str__(self):
        return "%s, %s" % (self.name, self.college)        




class User(models.Model):
    event=models.CharField(max_length=100)
    teamname= models.CharField(max_length=100)
    teamleader = models.CharField(max_length=100)
    Email= models.CharField(max_length=100)
    mob_no=models.CharField(max_length=15)
    year=models.CharField(max_length=15)
    college=models.CharField(max_length=15)     
    tmem1=models.CharField(max_length=100, blank=True)
    email1=models.CharField(max_length=100, blank=True)
    mob1=models.CharField(max_length=15, blank=True)
    tmem2=models.CharField(max_length=100, blank=True)
    email2=models.CharField(max_length=100, blank=True)
    mob2=models.CharField(max_length=100, blank=True)
    tmem3=models.CharField(max_length=100, blank=True)
    email3=models.CharField(max_length=100, blank=True)
    mob3=models.CharField(max_length=100, blank=True)
    tmem4=models.CharField(max_length=100, blank=True)
    email4=models.CharField(max_length=100, blank=True)
    mob4=models.CharField(max_length=100, blank=True)
    tmem5=models.CharField(max_length=100, blank=True)
    email5=models.CharField(max_length=100, blank=True)
    mob5=models.CharField(max_length=100, blank=True)
    query=models.CharField(max_length=100, blank=True)
      
    
    def __unicode__(self):
        return "%s, %s, %s" % (self.teamleader, self.college, self.event)

    def __str__(self):
        return "%s, %s, %s" % (self.teamleader, self.college, self.event)

                        

   



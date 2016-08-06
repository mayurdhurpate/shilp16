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
    designation = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    def __unicode__(self):
        return "%s, %s" % (self.author, self.title)
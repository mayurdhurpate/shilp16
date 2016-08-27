from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

class QUser(models.Model):
    name = models.CharField(_('name'), max_length=100)
    email = models.EmailField(_('email'), unique=True)
    phone = models.CharField(_('phone'), max_length=15)

    class Meta:
        verbose_name = _('quesr')
        verbose_name_plural = _('quesrs')

    def __unicode__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(_('name'), max_length=30, unique=True)
    password = models.CharField(max_length=40)
    slot = models.IntegerField(default=1)
    members = models.ManyToManyField(QUser)

    class Meta:
        verbose_name = _('team')
        verbose_name_plural = _('teams')

    def __unicode__(self):
        return self.name

class HelpQuestion(models.Model):
    name = models.CharField(_('name'), max_length=50)
    email = models.EmailField()
    message = models.TextField()
    resolved = models.BooleanField(_('resolved'), default=False)

    class Meta:
        verbose_name = _('Help Question')
        verbose_name_plural = _('Help Questions')

    def __unicode__(self):
        return self.name
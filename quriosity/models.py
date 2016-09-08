from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

class QUser(models.Model):
    name = models.CharField(_('name'), max_length=100)
    email = models.EmailField(_('email'), unique=True)
    phone = models.CharField(_('phone'), max_length=15)
    gender = models.CharField(_('gender'), max_length=5, blank=True, null=True)
    college = models.CharField(_('college'), max_length=50, blank=True, null=True)
    year = models.CharField(_('year'), max_length=5, blank=True, null=True)

    class Meta:
        verbose_name = _('quesr')
        verbose_name_plural = _('quesrs')

    def __unicode__(self):
        return self.name

class Question(models.Model):
    title = models.CharField(_('title'), max_length=30)
    content = models.TextField(_('content'))
    score = models.IntegerField(_('score'))
    answer = models.CharField(_('answer'), max_length=40)

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')

    def __unicode__(self):
        return self.title

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

class Response(models.Model):
    response = models.CharField(_('response'), max_length=40)
    question = models.ForeignKey(Question)
    team = models.ForeignKey(Team)

    class Meta:
        verbose_name = _('Response')
        verbose_name_plural = _('Responses')

    def __unicode__(self):
        return self.team.name

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

class Slot(models.Model):
    title = models.CharField(_('slot'), max_length=20)
    start = models.DateTimeField(_('start time'))
    end = models.DateTimeField(_('end time'))
    question = models.ManyToManyField(Question)

    class Meta:
        verbose_name = _('Slot')
        verbose_name_plural = _('Slots')

    def __unicode__(self):
        return self.title
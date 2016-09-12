from django.conf.urls import url
from quriosity.views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^help/$', helpQ, name='help'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^details/$', details, name='details'),
    url(r'^question/(?P<qid>[0-9]{,2})/$', question, name='question'),
    url(r'^secret/$', allu, name='allu'),
    url(r'^res/$', res, name='res'),
]
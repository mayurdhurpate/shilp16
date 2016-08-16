from django.conf.urls import url
from quriosity.views import *

urlpatterns = [
    url(r'^$', HomeView.as_view()),
    url(r'^signup/$', signup, name='signup')
]
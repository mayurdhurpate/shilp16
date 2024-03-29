"""shilp16 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^ca$', views.ca, name='ca'),
    url(r'^idp$', views.idp, name='idp'),
    url(r'^ppt$', views.ppt, name='ppt'),
    url(r'^gre$', views.gre, name='gre'),
    url(r'^alum$', views.alum, name='alum'),
    url(r'^conv$', views.conv, name='conv'),
    url(r'^Data-Analytics$', views.workshop1, name='Data-Analytics'),
    url(r'^Earthquake-Resistance-Structure$', views.workshop2, name='Earthquake-Resistance-Structure'),

    url(r'^register$', views.register, name='register'),
    url(r'^conclave$', views.conclave, name='conclave'),
    url(r'^worksubmit/$', views.worksubmit, name='worksubmit'),
    url(r'^workdatasubmit/$', views.worksubmit, name='worksubmit'),
    url(r'^gresubmit/$', views.gresubmit, name='gresubmit'),
    url(r'^regsubmit/$', views.regsubmit, name='regsubmit'),
    url(r'^casubmit/$', views.casubmit, name='casubmit'),
    url(r'^pptsubmit/$', views.pptsubmit, name='pptsubmit'),
    url(r'^team$',views.Staff, name='Staff'),
    url(r'^hospitality$',views.hospitality, name='hospitality'),
]

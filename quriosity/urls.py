from django.conf.urls import url
from quriosity.views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view()),
]
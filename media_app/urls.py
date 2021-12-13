from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^episode', views.Episode.as_view(), name="Episode"),
    url(r'^show', views.Show.as_view(), name="show"),
]

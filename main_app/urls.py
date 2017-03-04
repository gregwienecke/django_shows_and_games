from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^shows', views.shows),
	url(r'^post_url/$', views.post_game, name="post_game")
]
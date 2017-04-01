from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^shows', views.shows),
	url(r'^game_post_url/$', views.post_game, name="post_game"),
	url(r'^show_post_url/$', views.post_show, name="post_show"),
]
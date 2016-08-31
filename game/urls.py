from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^game/(?P<game_id>[0-9]+)/click_cell$', views.click_cell, name='click_cell'),
  url(r'^game/(?P<game_id>[0-9]+)/flag_cell$', views.flag_cell, name='flag_cell'),
  url(r'^game/(?P<game_id>[0-9]+)/unflag_cell$', views.unflag_cell, name='unflag_cell'),
  url(r'games$', views.create_game, name='create_game'),
  url(r'new_game$', views.new_game, name='new_game'),
]
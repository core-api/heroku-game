from django.conf.urls import url
from project.game.views import homepage, game_detail


urlpatterns = [
    url(r'^$', homepage),
    url(r'^(?P<pk>[0-9a-f-]+)$', game_detail)
]

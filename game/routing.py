## game/routing.py
from django.conf.urls import url
from game.consumers import TicTacToeConsumer

websocket_urlpatterns = [
    url(r'^ws/$', TicTacToeConsumer.as_asgi()),
]
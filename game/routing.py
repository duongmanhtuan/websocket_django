## game/routing.py
# from django.conf.urls import url
from django.urls import path
from game.consumers import TicTacToeConsumer

websocket_urlpatterns = [
    path('ws', TicTacToeConsumer.as_asgi()),
]
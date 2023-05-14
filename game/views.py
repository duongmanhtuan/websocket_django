# game/views.py
from django.shortcuts import render, redirect

def game(request, key):
    data = key
    return render(request, "game.html")
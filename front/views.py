from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from core.models import Deck


def dashboardView(request):
    return render(request, 'front/dashboard.html')


def settingsView(request):
    return render(request, 'front/settings.html')


def statisticsView(request):
    return render(request, 'front/statistics.html')


def deckView(request):
    return render(request, 'front/decks.html')


def deck_details_view(request, deck_id):
    deck = get_object_or_404(Deck, pk=deck_id)
    return render(request, 'front/deck_details.html', {'deck': deck})


def baseView(request):
    return render(request, "front/base.html")


def przykladView(request):
    return render(request, "front/przyklad.html")

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from core.models import Deck


def dashboardView(request):
    return render(request, "front/dashboard.html")


def settingsView(request):
    return render(request, "front/settings.html")


def statisticsView(request):
    return render(request, "front/statistics.html")


def decksListView(request):
    return render(request, "front/decks.html")


def deckView(request, deck_id):
    deck = get_object_or_404(Deck, pk=deck_id)
    return render(request, "front/deck_menu.html", {"deck": deck})


def flashCardView(request):
    return HttpResponse("ahjo flashCard_id")


def deckEditView(request, deck_id):
    deck = get_object_or_404(Deck, pk=deck_id)
    return render(request, "front/deck_edit.html", {"deck": deck})


def baseView(request):
    return render(request, "front/base.html")


def przykladView(request):
    return render(request, "front/przyklad.html")

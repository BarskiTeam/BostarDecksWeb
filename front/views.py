from django.shortcuts import render


def dashboardView(request):
    return render(request, "front/dashboard.html")


def settingsView(request):
    return render(request, "front/settings.html")


def statisticsView(request):
    return render(request, "front/statistics.html")


def deckView(request):
    return render(request, "front/decks.html")


def baseView(request):
    return render(request, "front/base.html")


def przykladView(request):
    return render(request, "front/przyklad.html")

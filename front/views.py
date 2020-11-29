from django.http import HttpResponse
from django.shortcuts import render


def startView(request):
    return HttpResponse("start")


def loginView(request):
    return HttpResponse("login")


def dashboardView(request):
    return HttpResponse("dashboard")


def deckView(request):
    return HttpResponse("deck")


def baseView(request):
    return render(request, "front/base.html")


def przykladView(request):
    return render(request, "front/przyklad.html")

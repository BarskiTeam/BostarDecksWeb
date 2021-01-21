from django.urls import path

from . import views
from .apps import FrontConfig

app_name = FrontConfig.name
urlpatterns = [
    path("", views.dashboardView, name="dashboard"),
    path("dashboard", views.dashboardView, name="dashboard"),
    path("decks", views.deckView, name="deck"),
    path("settings", views.settingsView, name="settings"),
    path("statistics", views.statisticsView, name="statistics"),
    path("przyklad", views.przykladView, name="przyklad"),
    path("base", views.baseView, name="base"),
]

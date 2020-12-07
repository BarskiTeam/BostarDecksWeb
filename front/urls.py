from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboardView, name="dashboard"),
    path('dashboard', views.dashboardView, name="dashboard"),
    path('decks', views.deckView, name="deck"),
    path('decks/details/<int:deck_id>', views.deck_details_view, name="deck_detail"),
    path('settings', views.settingsView, name="settings"),
    path('statistics', views.statisticsView, name="statistics"),
    path('przyklad', views.przykladView, name="przyklad"),
    path('base', views.baseView, name="base")
]

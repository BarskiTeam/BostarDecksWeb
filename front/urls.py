from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.startView, name="start"),
    path('start', views.startView, name="start"),
    path('login', views.loginView, name="login"),
    path('', views.dashboardView, name="dashboard"),
    path('dashboard', views.dashboardView, name="dashboard"),
    path('decks', views.deckView, name="deck"),
    path('settings', views.settingsView, name="settings"),
    path('statistics', views.statisticsView, name="statistics"),
    path('przyklad', views.przykladView, name="przyklad"),
    path('base', views.baseView, name="base")
]

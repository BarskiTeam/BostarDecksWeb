from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.startView, name="start"),
    path('login', views.loginView, name="login"),
    path('dashboard', views.dashboardView, name="dashboard"),
    path('deck', views.deckView, name="deck"),
]

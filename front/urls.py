from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.startView, name="start"),
    path('start', views.startView, name="start"),
    path('login', views.loginView, name="login"),
    path('dashboard', views.dashboardView, name="dashboard"),
    path('deck', views.deckView, name="deck"),
    path('przyklad', views.przykladView, name="przyklad"),
    path('base', views.baseView, name="base")
]

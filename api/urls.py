from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'deck', views.DeckViewSet)
router.register(r'flashCard', views.FlashCardViewSet)
router.register(r'deckFlashCard', views.DeckFlashCardViewSet)
router.register(r'level', views.LevelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

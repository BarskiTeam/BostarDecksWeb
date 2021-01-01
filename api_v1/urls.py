from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .apps import ApiV1Config

app_name = ApiV1Config.name

router = DefaultRouter()
router.register(r"user", views.UserViewSet)
router.register(r"deck", views.DeckViewSet)
router.register(r"flashcard", views.FlashcardViewSet)
router.register(r"deckflashcard", views.DeckFlashcardViewSet)
router.register(r"level", views.LevelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

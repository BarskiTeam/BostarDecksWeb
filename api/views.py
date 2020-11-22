from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from core.models import (
    Deck, DeckFlashCard, FlashCard, Level
)
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    DeckSerializer, DeckFlashCardSerializer,
    FlashCardSerializer, LevelSerializer, UserSerializer
)

# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'user': reverse('user-list', request=request, format=format),
        'deck': reverse('deck-list', request=request, format=format),
        'deckFlashCard': reverse('deckFlashCard-list', request=request,
                                 format=format),
        'flashCard': reverse('flashCard-list', request=request,
                             format=format),
        'level': reverse('level-list', request=request,
                         format=format)
    })


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
         serializer.save(owner=self.request.user)


class FlashCardViewSet(viewsets.ModelViewSet):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class DeckFlashCardViewSet(viewsets.ModelViewSet):
    queryset = DeckFlashCard.objects.all()
    serializer_class = DeckFlashCardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
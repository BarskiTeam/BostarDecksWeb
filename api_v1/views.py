from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse

from core.models import (
    Deck, DeckFlashcard, Flashcard, Level, User
)
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    DeckSerializer, DeckFlashcardSerializer,
    FlashcardSerializer, LevelSerializer, UserSerializer
)


# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'user': reverse('user-list', request=request, format=format),
        'deck': reverse('deck-list', request=request, format=format),
        'deckflashcard': reverse('deckflashcard-list', request=request,
                                 format=format),
        'flashcard': reverse('flashcard-list', request=request,
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

    # example destination_url of this view : http://127.0.0.1:8000/api/v1/deck/1/flashcards/
    @action(methods=['get'], detail=True, permission_classes=[IsOwnerOrReadOnly])
    def flashcards(self, request, pk):
        deck = Deck.objects.get(id=pk)
        flashcard = deck.flashcard
        serializer = FlashcardSerializer(flashcard, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FlashcardViewSet(viewsets.ModelViewSet):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class DeckFlashcardViewSet(viewsets.ModelViewSet):
    queryset = DeckFlashcard.objects.all()
    serializer_class = DeckFlashcardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

import json

from django.test.client import encode_multipart, RequestFactory
from rest_framework.test import APITestCase, URLPatternsTestCase

from core.models import DeckFlashcard, Flashcard, Deck
from core.factories import DeckFlashcardFactory, DeckFactory, FlashcardFactory
from api_v1.views import DeckViewSet


class DeckTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.deck_num = 20
        cls.flashcard_num = 20
        cls.deck = DeckFactory.create_batch(cls.deck_num)
        for i in cls.deck:
            i.flashcard.set(FlashcardFactory.create_batch(cls.flashcard_num))

    def test_list_deck(self):
        request = RequestFactory().get("/api_v1/")
        view = DeckViewSet.as_view({"get": "list"})
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), self.deck_num)

    def test_retrieve_deck(self):
        pk = 1
        obj = Deck.objects.get(id=pk)
        request = RequestFactory().get(f"/api_v1/{pk}")
        view = DeckViewSet.as_view({"get": "retrieve"})
        response = view(request, pk=pk)
        response.render()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 7)  # number of fields
        self.assertEqual(response.data["id"], obj.id)
        self.assertEqual(response.data["owner"], obj.owner.username)
        self.assertEqual(response.data["name"], obj.name)
        self.assertEqual(response.data["description"], obj.description)
        self.assertEqual(response.data["tag"], obj.tag)
        self.assertEqual(response.data["public"], obj.public)
        self.assertEqual(
            response.data["flashcard"], list(obj.flashcard.values_list("id", flat=True))
        )

# Create your tests here.

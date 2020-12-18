import pytest
from .. import factories
from ..models import Deck, Flashcard, Level, DeckFlashcard, User

pytestmark = pytest.mark.django_db


class TestFactories:
    def test_deck_create(self):
        factories.DeckFactory.create()
        assert Deck.objects.count() == 1, "Should create one deck"
        assert User.objects.count() == 1, "Should create one user"
        assert Flashcard.objects.count() == 0, "Shouldn't create any flashcard"
        assert Level.objects.count() == 0, "Shouldn't create any level"
        assert DeckFlashcard.objects.count() == 0, "Shouldn't create any DeckFlashcard"

    def test_flashcard_create(self):
        factories.FlashcardFactory.create()
        assert Deck.objects.count() == 0, "Shouldn't create any deck"
        assert User.objects.count() == 0, "Shouldn't create any user"
        assert Flashcard.objects.count() == 1, "Should create flashcard"
        assert Level.objects.count() == 0, "Shouldn't create any level"
        assert DeckFlashcard.objects.count() == 0, "Shouldn't create any DeckFlashcard"

    def test_level_create(self):
        factories.LevelFactory.create()
        assert Level.objects.count() == 1, "Should create one level"
        assert Deck.objects.count() == 0, "Shouldn't create any deck"
        assert User.objects.count() == 0, "Shouldn't create any user"
        assert Flashcard.objects.count() == 0, "Shouldn't create any flashcard"
        assert DeckFlashcard.objects.count() == 0, "Shouldn't create any DeckFlashcard"

    def test_deck_flashcard_create(self):
        factories.DeckFlashcardFactory.create()
        assert Level.objects.count() == 1, "Should create one level"
        assert Deck.objects.count() == 1, "Should create one deck"
        assert User.objects.count() == 1, "Should create one user"
        assert Flashcard.objects.count() == 1, "Should create one flashcard"
        assert DeckFlashcard.objects.count() == 1, "Should create one DeckFlashcard"

    def test_user_create(self):
        factories.UserFactory.create()
        assert User.objects.count() == 1, "Should create one user"
        assert Level.objects.count() == 0, "Shouldn't create any level"
        assert Deck.objects.count() == 0, "Shouldn't create any deck"
        assert Flashcard.objects.count() == 0, "Shouldn't create any flashcard"
        assert DeckFlashcard.objects.count() == 0, "Shouldn't create any DeckFlashcard"
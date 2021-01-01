from rest_framework import serializers
from core.models import Deck, DeckFlashcard, Flashcard, Level, User


class DeckSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Deck
        fields = "__all__"


class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = "__all__"


class DeckFlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeckFlashcard
        fields = "__all__"


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

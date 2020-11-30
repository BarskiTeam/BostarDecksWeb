
from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import (
    Deck, DeckFlashCard, FlashCard, Level
)


class DeckSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Deck
        fields = "__all__"


class FlashCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCard
        fields = "__all__"


class DeckFlashCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeckFlashCard
        fields = "__all__"


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
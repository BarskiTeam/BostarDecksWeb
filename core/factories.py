import factory
import factory.fuzzy
from core import models


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    username = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    is_superuser = False


class DeckFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Deck

    name = factory.Sequence(lambda n: "deck%s" % n)
    description = factory.Sequence(lambda n: "description%s" % n)
    tag = factory.Sequence(lambda n: "tag%s" % n)
    owner = factory.SubFactory(UserFactory)


class FlashcardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Flashcard

    name = factory.Sequence(lambda n: "flashcard%s" % n)
    reverse = factory.Sequence(lambda n: "reverse%s" % n)
    averse = factory.Sequence(lambda n: "averse%s" % n)
    tip = factory.Sequence(lambda n: "tip%s" % n)


class LevelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Level

    name = factory.Sequence(lambda n: "level%s" % n)
    repeat_frequency = factory.fuzzy.FuzzyInteger(0, 1000)


class DeckFlashcardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.DeckFlashcard

    deck = factory.SubFactory(DeckFactory)
    flashcard = factory.SubFactory(FlashcardFactory)
    level = factory.SubFactory(LevelFactory)
    good_answers = factory.fuzzy.FuzzyInteger(0, 1000)
    bad_answers = factory.fuzzy.FuzzyInteger(0, 1000)

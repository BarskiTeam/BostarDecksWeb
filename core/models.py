from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Deck(models.Model):
    name = models.CharField(max_length=100, verbose_name="name of deck")
    description = models.CharField(max_length=1200, verbose_name="Description of deck")
    tag = models.CharField(max_length=50, verbose_name="tag")
    flashCard = models.ManyToManyField('FlashCard', related_name='flashCard', through='DeckFlashCard')
    public = models.BooleanField(default=False)
    owner = models.ForeignKey("User", related_name="deck", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Deck"
        verbose_name_plural = "Decks"
        ordering = ['name']


class DeckFlashCard(models.Model):
    deck = models.ForeignKey('Deck', on_delete=models.SET_NULL, null=True)
    flashCard = models.ForeignKey('FlashCard', on_delete=models.SET_NULL, null=True)
    level = models.ForeignKey('Level', on_delete=models.SET_NULL, null=True)
    good_answers = models.IntegerField(verbose_name="good answers", default=0)
    bad_answers = models.IntegerField(verbose_name="bad answers", default=0)

    def __str__(self):
        return str("" + self.deck.name +" "+  self.flashCard.name)

    class Meta:
        verbose_name = "DeckFlashCard"
        verbose_name_plural = "DeckFlashCards"
        ordering = ['id']


class FlashCard(models.Model):
    name = models.CharField(max_length=100, verbose_name="name of flashcard")
    reverse = models.CharField(max_length=1200, verbose_name="Revers of card")
    averse = models.CharField(max_length=1200, verbose_name="Avers of card")
    tip = models.CharField(max_length=100, verbose_name="Tip for flash card")
    deck = models.ManyToManyField('Deck', related_name='deck', through='DeckFlashCard')
    #tag = lista tagów/stringow

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Flash Card"
        verbose_name_plural = "Flash Cards"
        ordering = ['name']


class Level(models.Model):
    name = models.CharField(max_length=100, verbose_name="name of levels")
    repeat_frequency = models.IntegerField(verbose_name="time of frequency")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Level"
        verbose_name_plural = "Levels"
        ordering = ['id']

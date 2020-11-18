from django.contrib import admin

# Register your models here.
from .models import Deck, DeckFlashCard, \
    FlashCard, Level

admin.site.register(Deck)
admin.site.register(DeckFlashCard)
admin.site.register(FlashCard)
admin.site.register(Level)

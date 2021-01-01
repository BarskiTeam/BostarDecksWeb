from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import User

# Register your models here.
from .models import Deck, DeckFlashcard, Flashcard, Level

admin.site.register(Deck)
admin.site.register(DeckFlashcard)
admin.site.register(Flashcard)
admin.site.register(Level)
admin.site.register(User, UserAdmin)

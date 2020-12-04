from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import User

# Register your models here.
from .models import Deck, DeckFlashCard, \
    FlashCard, Level

admin.site.register(Deck)
admin.site.register(DeckFlashCard)
admin.site.register(FlashCard)
admin.site.register(Level)
admin.site.register(User, UserAdmin)

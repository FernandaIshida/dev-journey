from django.contrib import admin

from .models import Gamer, Game, Friend

class Gamers(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'steam_username', 'country', 'join_date',)
    list_display_links = ('id', 'nickname',)
    list_per_page = 20
    search_fields = ('nickname', 'steam_username', 'country',)
    ordering = ('nickname',)

admin.site.register(Gamer, Gamers)

class Games(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'studio', 'release_date', 'playtime_minutes',)
    list_display_links = ('id', 'title',)
    list_per_page = 20
    search_fields = ('title', 'genre', 'studio',)
    ordering = ('title',)

admin.site.register(Game, Games)

class FriendInline(admin.TabularInline):
    model = Friend
    extra = 0
    readonly_fields = ['match_score', 'top_games']

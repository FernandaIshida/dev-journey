from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from steam_match.models import Gamer, Game
from steam_match.serializers import GamerSerializer, GameSerializer

class GamerViewSet(viewsets.ModelViewSet):
    queryset = Gamer.objects.all()
    serializer_class = GamerSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nickname', 'join_date']
    search_fields = ['nickname', 'steam_username', 'country']

class GameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['title', 'release_date', 'playtime_minutes']
    search_fields = ['title', 'genre', 'studio']        

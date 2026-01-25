from rest_framework import serializers
from steam_match.models import Gamer, Game, Friend

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['title', 'genre', 'studio', 'release_date', 'playtime_minutes', 'playtime_hours']
        read_only_fields = ['title', 'genre', 'studio', 'release_date', 'playtime_minutes', 'playtime_hours']

class FriendNestedSerializer(serializers.ModelSerializer):
    top_games = GameSerializer(many=True, read_only=True)
    class Meta: 
        model = Friend
        fields = ['steam_username', 'match_score', 'top_games']
        read_only_fields = ['steam_username', 'match_score', 'top_games']    
    def get_top_games(self, obj):
        return GameSerializer(obj.top_games.all(), many=True).data

class GamerSerializer(serializers.ModelSerializer):
    friends = FriendNestedSerializer(many=True, read_only=True)
    class Meta:
        model = Gamer
        fields = ['nickname', 'steam_username', 'avatar_url', 'country', 'join_date', 'friends']
        read_only_fields = ['join_date', 'friends']
        
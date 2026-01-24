from django.db import models

class Gamer(models.Model):
    nickname = models.CharField(max_length=30, unique=True)
    steam_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
    avatar_url = models.URLField(blank=True, null=True)
    country = models.CharField(max_length=30, blank=True)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.nickname} ({self.steam_id})' if self.steam_id else self.nickname
    
class Game(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    studio = models.CharField(max_length=50)
    release_date = models.DateField(blank=True, null=True)
    playtime_minutes = models.IntegerField(default=0)
    
    @property
    def playtime_hours(self):
        return round(self.playtime_minutes / 60, 1)
    def __str__(self):
        return self.title
    
class Friend(models.Model):
    gamer = models.ForeignKey( Gamer, related_name='friends', on_delete=models.CASCADE)
    steam_nickname = models.CharField(max_length=30)
    match_score = models.IntegerField(default=0)
    top_games = models.ManyToManyField(Game, blank=True)

    def __str__(self):
        return f'Friend: {self.steam_nickname}'
    

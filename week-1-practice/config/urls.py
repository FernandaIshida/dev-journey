from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from steam_match.views import GameViewSet, GamerViewSet

router = routers.DefaultRouter()
router.register('gamers', GamerViewSet, basename='gamers')
router.register('games', GameViewSet, basename='games')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

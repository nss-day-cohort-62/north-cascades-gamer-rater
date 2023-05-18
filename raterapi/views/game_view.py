"""View module for handling requests for customer data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterapi.models import Game


class GameView(ViewSet):
    def list(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def create(self, request):
        game = Game.objects.create(
            title=request.data['title'],
            designer=request.data['designer'],
            year_released=request.data['year_released'],
            number_of_players=request.data['number_of_players'],
            age_recommendation=request.data['age_recommendation'],
            time_to_play=request.data['time_to_play']
        )

        game.categories.set(request.data['categories'])

        serializer = GameSerializer(game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title', 'designer', 'year_released', 'number_of_players',
                  'time_to_play', 'age_recommendation', 'categories')
        depth = 1

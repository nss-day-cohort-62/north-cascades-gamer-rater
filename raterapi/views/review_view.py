"""View module for handling requests for customer data"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterapi.models import Review, Game, Player


class ReviewView(ViewSet):
    def list(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        game = Game.objects.get(pk=request.data['game'])
        player = Player.objects.get(user=request.auth.user)
        review = Review.objects.create(
            description=request.data['description'],
            rating=request.data['rating'],
            player=player,
            game=game
        )

        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        game = Game.objects.get(pk=request.data['game'])
        player = Player.objects.get(user=request.auth.user)
        review = Review.objects.get(pk=pk)
        review.description = request.data['description']
        review.rating = request.data['rating']
        review.player = player
        review.game = game
        review.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        review = Review.objects.get(pk=pk)
        review.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'description', 'rating', 'player', 'game')
        depth = 2

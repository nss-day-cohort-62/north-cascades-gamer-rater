from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterapi.models import Image, Player, Game


class ImageView(ViewSet):
    def list(self, request):
        images = Image.objects.all()
        serialized = ImageSerializer(images, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        image = Image.objects.get(pk=pk)
        serialized = ImageSerializer(image)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        game = Game.objects.get(pk=request.data['game'])
        player = Player.objects.get(user=request.auth.user)

        image = Image.objects.create(
            game = game,
            player = player,
            image = request.data["images"]
        )

        serializer = ImageSerializer(image)
        return Response (serializer.data, status=status.HTTP_201_CREATED)
         


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('bio', )


class ImageSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()

    class Meta:
        model = Image
        fields = ('game', 'image', 'player')

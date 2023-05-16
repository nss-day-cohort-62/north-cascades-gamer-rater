from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterapi.models import Image, Player


class ImageView(ViewSet):
    def list(self, request):
        images = Image.objects.all()
        serialized = ImageSerializer(images, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        image = Image.objects.get(pk=pk)
        serialized = ImageSerializer(image)
        return Response(serialized.data, status=status.HTTP_200_OK)


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('bio', )


class ImageSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()

    class Meta:
        model = Image
        fields = ('game', 'image', 'player')

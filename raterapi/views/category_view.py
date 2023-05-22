"""View module for handling requests for customer data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterapi.models import Category


class CategoryView(ViewSet):
    def list(self, request):
        """Handles GET requests to get all categories, returns JSON serialized list of categories"""
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handles GET requests for single category, returns JSON serialized category"""

        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handles POST operations and returns JSON serialized category"""
        category = Category.objects.create(
            description=request.data['description'],
        )

        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handles DELETE request for pets, Response: None with 204 status code"""
        category = Category.objects.get(pk=pk)
        category.description = request.data['description']
        category.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('description', 'id')

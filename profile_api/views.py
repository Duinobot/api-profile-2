from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status #return HTTP responses
from rest_framework import viewsets

from profile_api import serializers
from profile_api import models

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions',
            'Similar to noraml Django View',
            'Give us most control over our apps',
            'Mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """create a hello message using name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello, {name}"
            return Response({'message':message})
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        a_viewset = [
            "use actions (list, create, retrieve, update, partial_update) as class methods",
            "Automatically maps to URLs using Routers",
            "Provides more functionalities with less code",
        ]

        return Response({'message':'hello','a_viewset':a_viewset})

    def create(self, request):
        
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, retrieve, pk=None):
        return Response({'Method':'get'})

    def update(self, request, pk=None):
        return Response({'Method':'put'})

    def partial_update(self, request, pk=None):
        return Response({'Method':'patch'})

    def destroy(self, request, pk=None):
        return Response({'Method':'delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handles profile creation and update"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()


from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions',
            'Similar to noraml Django View',
            'Give us most control over our apps',
            'Mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
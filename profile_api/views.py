from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """Return a list of APIView Features"""
        an_apiview = [
            'User HTTP methods as function (get ,post,paych ,put,delete )',
            'is similar to a traditional Django view',
            'Gives you the control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello !', 'an_apiview': an_apiview})

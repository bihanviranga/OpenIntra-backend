from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class UnprotectedView(APIView):
    def get(self, request):
        response = {'message' : 'Unprotected view'}
        return Response(response)

class ProtectedView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        response = {'message': 'Protected view'}
        return Response(response)


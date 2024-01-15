from rest_framework import generics, authentication, permissions, status
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response

class DashboardView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        return Response(status = status.HTTP_200_OK)

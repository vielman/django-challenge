from rest_framework import generics, authentication, permissions, status
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken 
from users.serializers import UserSerializer, AuthTokenSerializer
from users.models import User

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class ListUserView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

class RetreiveUpdateUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class CreateTokenView(ObtainAuthToken):
    """Vista para crear un token"""
    serializer_class = AuthTokenSerializer

class Logout(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status = status.HTTP_200_OK)

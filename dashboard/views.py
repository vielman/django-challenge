from rest_framework import generics, authentication, permissions, status
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd

class DashboardView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):

        df = pd.read_csv('DataRedesSociales.csv', usecols=['text'])
        df.head()
        df.iloc[0].values
        
        return Response(df.iloc[0].values,status = status.HTTP_200_OK)

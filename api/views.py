from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import RegisterSerializer, LoginSerializer
from rest_framework import status
from django.contrib.auth import authenticate
from api.models import User




class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)    

        if serializer.is_valid():
            User.objects.create_user(**serializer.validated_data)
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            if user:
                return Response({"message": "Login successful"})
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

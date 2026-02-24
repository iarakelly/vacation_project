from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login
from django.http import JsonResponse
from django.views import View
from django.contrib.auth import get_user_model, authenticate
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated 

from rest_framework.authtoken.models import Token 

User = get_user_model()

class RegisterView(APIView):


    def post(self, request):
        data = request.data
        
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        user = User.objects.create_user(
            username = username, 
            email = email, 
            password = password
        )
            
        return Response(
            {
                "id": user.pk,
                "username": user.username,
                "email": user.email
            },
            status=status.HTTP_201_CREATED
        )
# Create your views here.

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:

            token, created = Token.objects.get_or_create(user=user)

            return Response({"message" : "Login realizado", "user_id" : user.pk, "username": user.username, 
                             "token" : token.key},
                            status = status.HTTP_200_OK)
        
        return Response(
            {"error": "Credenciais inválidas"},
            status=status.HTTP_400_BAD_REQUEST
        )

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        return Response ({"message" : "seus dados", "user": user.username, "email": user.email})

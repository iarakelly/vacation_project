from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from rest_framework.views import APIView

from rest_framework import status

from rest_framework.response import Response


class RegisterView(APIView):
    def post(self, request):

        name = request.data.get('name:')
        email = request.data.get('email:')
        password = request.data.get('password:')

        user = User.objects.create(name = name, email = email, password = password)
            
        return Response(
            {
                "id": user.id,
                "name": user.name,
                'email': user.emailUser
            },
            status=status.HTTP_201_CREATED
        )
# Create your views here.

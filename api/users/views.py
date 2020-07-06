from django.shortcuts import render
from rest_framework import viewsets

from api.users.models import User, UserSerializer


class Users(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

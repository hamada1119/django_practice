from rest_framework import serializers, viewsets
from django.shortcuts import render
from .models import Message
from .serializer import MessageSerializer

class MessageViewset(viewsets.ModelViewSet):
    serializer_class=MessageSerializer
    queryset=Message.objects.all()








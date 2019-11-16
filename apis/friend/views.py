from django.shortcuts import render
from rest_framework import generics,permissions
from apis.friend.serializer import FriendSerializer
from apis.friend.models import Friend

# Create your views here.
class CreateFriendAPIView(generics.CreateAPIView):
    
    serializer_class = FriendSerializer 
    permission_classes =[permissions.IsAuthenticated]

class UpdateFriendAPIView(generics.UpdateAPIView):
    
    serializer_class = FriendSerializer 
    permission_classes =[permissions.IsAuthenticated]
    queryset = Friend.objects.all()

class SingleFriendAPIView(generics.RetrieveAPIView):
    serializer_class = FriendSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Friend.objects.all()

class ListFriendAPIView(generics.ListAPIView):
    serializer_class = FriendSerializer
    queryset = Friend.objects.all()
    #pagination_class = PageNumberPagination

class DeleteFriendAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Friend.objects.all()

 
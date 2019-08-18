from django.shortcuts import render
from rest_framework import generics,permissions
from apis.friends.serializer import FriendsSerializer
from apis.friends.models import Friends

# Create your views here.
class CreateFriendsAPIView(generics.CreateAPIView):
    
    serializer_class = FriendsSerializer 
    permission_classes =[permissions.IsAuthenticated]

class UpdateFriendsAPIView(generics.UpdateAPIView):
    
    serializer_class = FriendsSerializer 
    permission_classes =[permissions.IsAuthenticated]
    queryset = Friends.objects.all()

class SingleFriendsAPIView(generics.RetrieveAPIView):
    serializer_class = FriendsSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Friends.objects.all()

class ListFriendsAPIView(generics.ListAPIView):
    serializer_class = FriendsSerializer
    queryset = Friends.objects.all()
    #pagination_class = PageNumberPagination

class DeleteFriendsAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Friends.objects.all()

 
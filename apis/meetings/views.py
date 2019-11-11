from django.shortcuts import render
from rest_framework import generics,permissions
from apis.meetings.serializer import MeetingsSerializer
from apis.meetings.models import Meetings

#Create your views here.
class CreateMeetingsAPIView(generics.CreateAPIView):
    
    serializer_class = MeetingsSerializer 
    permission_classes =[permissions.IsAuthenticated]

class UpdateMeetingsAPIView(generics.UpdateAPIView):

    serializer_class = MeetingsSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Meetings.objects.all()

class SingleMeetingsAPIView(generics.RetrieveAPIView):
    serializer_class = MeetingsSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Meetings.objects.all()
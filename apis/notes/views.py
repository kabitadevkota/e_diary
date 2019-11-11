
from django.shortcuts import render
from rest_framework import generics,permissions
from apis.notes.serializer import NotesSerializer
from apis.notes.models import Notes

# Create your views here.
class CreateNotesAPIView(generics.CreateAPIView):
    
    serializer_class = NotesSerializer 
    permission_classes =[permissions.IsAuthenticated]

# Create your views here.

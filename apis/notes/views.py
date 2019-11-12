
from django.shortcuts import render
from rest_framework import generics,permissions
from apis.notes.serializer import NotesSerializer
from apis.notes.models import Notes

# Create your views here.
class CreateNotesAPIView(generics.CreateAPIView):
    
    serializer_class = NotesSerializer 
    permission_classes =[permissions.IsAuthenticated]

class UpdateNotesAPIView(generics.UpdateAPIView):
    
    serializer_class = NotesSerializer 
    permission_classes =[permissions.IsAuthenticated]
    queryset = Notes.objects.all()

class SingleNotesAPIView(generics.RetrieveAPIView):
    serializer_class = NotesSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Notes.objects.all()

class ListNotesAPIView(generics.ListAPIView):
    serializer_class = NotesSerializer
    queryset = Notes.objects.all()
    #pagination_class = PageNumberPagination

class DeleteNotesAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Notes.objects.all()

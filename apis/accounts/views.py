from django.shortcuts import render, get_object_or_404
from apis.accounts.serializer import UserSerializer, UpdateUserSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework import permissions
from apis.accounts.models import Users
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.
class CreateUserApiView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


# Create your views here.
class UpdateUserApiView(UpdateAPIView):
    serializer_class = UpdateUserSerializer
    queryset = Users.objects.all()
    permission_classes =[permissions.IsAuthenticated]

@api_view(["GET"])
def user_posts(request,*args,**kwargs):
    user_id= kwargs.get('pk')
    users = get_object_or_404(Users,pk = user_id)
    serializer= UserSerializer(users)
    return Response(serializer.data, status=status.HTTP_200_OK)
    


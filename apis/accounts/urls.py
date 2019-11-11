from django.urls import path
from apis.accounts import views

urlpatterns = [
    path("users/", views.CreateUserApiView.as_view()),
    path("users/<int:pk>/", views.UpdateUserApiView.as_view())
    
]
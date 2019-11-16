from django.urls import path
from apis.friend import views 

urlpatterns = [
    path("create/", views.CreateFriendAPIView.as_view()),
    path("<int:pk>/update/", views.UpdateFriendAPIView.as_view()),
    path("<int:pk>/delete/", views.DeleteFriendAPIView.as_view()),
    path("<int:pk>/", views.SingleFriendAPIView.as_view()),
    path("", views.ListFriendAPIView.as_view()),
    
]
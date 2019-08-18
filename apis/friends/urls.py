from django.urls import path
from apis.friends import views 

urlpatterns = [
    path("create/", views.CreateFriendsAPIView.as_view()),
    path("<int:pk>/update/", views.UpdateFriendsAPIView.as_view()),
    path("<int:pk>/delete/", views.DeleteFriendsAPIView.as_view()),
    path("<int:pk>/", views.SingleFriendsAPIView.as_view()),
    path("", views.ListFriendsAPIView.as_view()),
    
]
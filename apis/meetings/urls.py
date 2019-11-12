from django.urls import path
from apis.meetings import views 

urlpatterns = [
    path("create/", views.CreateMeetingsAPIView.as_view()),
    path("<int:pk>/update/", views.UpdateMeetingsAPIView.as_view()),
    path("<int:pk>/delete/", views.DeleteMeetingsAPIView.as_view()),
    path("<int:pk>/", views.SingleMeetingsAPIView.as_view()),
    path("", views.ListMeetingsAPIView.as_view()),
    


]
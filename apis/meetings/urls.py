from django.urls import path
from apis.meetings import views 

urlpatterns = [
    path("create/", views.CreateMeetingsAPIView.as_view()),
    


]
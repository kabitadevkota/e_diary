from django.urls import path
from apis.notes import views 

urlpatterns = [
    path("create/", views.CreateNotesAPIView.as_view()),
]
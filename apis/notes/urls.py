from django.urls import path
from apis.notes import views 

urlpatterns = [
    path("create/", views.CreateNotesAPIView.as_view()),
    path("<int:pk>/update/", views.UpdateNotesAPIView.as_view()),
    path("<int:pk>/delete/", views.DeleteNotesAPIView.as_view()),
    path("<int:pk>/", views.SingleNotesAPIView.as_view()),
    path("", views.ListNotesAPIView.as_view()),
]
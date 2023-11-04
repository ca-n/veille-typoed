from django.urls import path

from tests import views

urlpatterns = [
    path("", views.HighscoreList.as_view()),
]
"""
URL configuration for typoed project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from tests.views import *
from users.views import *

urlpatterns = [
    path('register/', UserCreate.as_view()),
    path('highscores/', HighscoreList.as_view()),
    path('user/<str:pk>/', UserDetail.as_view()),
    path('user/<str:pk>/edit', UserUpdate.as_view()),
    path('user/<str:pk>/delete', UserDelete.as_view()),
    path('admin/', admin.site.urls),
]

"""StudentHomepage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.LoginView.as_view(), name='login'),

    path('reg/', views.reg, name='reg'),
    path('logout/', views.logout, name='logout'),
    path('photo_album/', views.photo_album, name='photo_album'),
    path('home/', views.home, name='home'),
    path('school/', views.school, name='school'),
    path('hobby/', views.Hobby.as_view()),
    path('admirer/', views.Admirer.as_view()),
    path('reading_matter/', views.ReadingMatter.as_view()),
]

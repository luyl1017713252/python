"""bms_2 URL Configuration

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
from django.urls import path, re_path

from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.books, name='books'),
    path('book/add/', views.add_book),
    re_path('book/del/', views.del_book),
    re_path('book/update/(\d+)', views.up_book),
    path('publishs/', views.publishs),
    path('publish/add/', views.add_publish),
    re_path('publish/del/(\d+)', views.del_publish),
    re_path('publish/update/(\d+)', views.up_publish),
    path('authors/', views.authors),
    path('author/add/', views.add_author),
    re_path('author/del/(\d+)', views.del_author),
    re_path('author/update/(\d+)', views.up_author),
    re_path('ajax_add_book', views.ajax_add_book)

]

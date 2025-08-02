"""
URL configuration for student_demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from student_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/",views.registeruser,name='register'),
    path("",views.loginuser),
    path("login/",views.loginuser),
    path('insert/', views.insertdata, name='insert'),
    path('update/', views.updatedata, name='update'), 
     path('search/', views.searchdata, name='search'),
    path('delete/', views.deletedata, name='delete'),
        path('top3/', views.top_scorers, name='top3'),
            path('index/', views.index, name='index'), 

        


]

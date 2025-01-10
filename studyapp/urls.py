"""
URL configuration for learndjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.urls import path, include
from . import views

urlpatterns = [
    path('web1', views.stud, name='web1'),
    path('test1', views.test, name='test'),
    path('studtest', views.studtest, name='studtest'),
    path('allstudy', views.allstudy, name='allstudy'),
    path('update/<int:id>/', views.studentUpdate,name='student_update'),
    path('delete/<int:id>/', views.deletestudy,name='student_delete'),
]


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
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('create',views.student_create,name='student_create'),
    path('<int:id>/', views.student_detail,name='student_detail'),
    # path('<int:id>/edit/', views.student_update,name='student_update'),
    # path('<int:id>/delete/', views.student_delete,name='student_delete'),


]


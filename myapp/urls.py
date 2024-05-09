"""
URL configuration for digitalsociety project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
     path('', views.login, name='login'),
     path('logout/', views.logout, name='logout'),
     path('profile/', views.profile, name='profile'),
     path('member/profile/', views.memberProfile, name='mprofile'),
     path('change_pass/', views.change_pass, name='change_pass'),
     path('pedit/', views.pedit, name='pedit'),
     path('member/profile/edit/', views.mempedit, name='mpedit'),
     path('addmember/', views.addMember, name='addmember'),
     path('allmember/', views.allSocietymembers, name='allmember'),
     path('forget_pass/', views.forget_pass, name='forget_pass'),
     path('email_verify/', views.email_verify, name='email_verify'),
     path('new_pass/', views.new_pass, name='new_pass'),
     path('all_members/', views.allSocietymembers, name='all_mems'),
]

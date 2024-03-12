from django.conf.urls import url
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from . import views
from django.urls import path, include

app_names='accounts'

urlpatterns = [
     path('login/',LoginView.as_view(redirect_authenticated_user=True,
     template_name='account/login.html'
     ),name='login'),
     path('logout/',LogoutView.as_view(),name='logout'),
]



"""
 #path('',views.index,name='name'),
 #path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
 #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
 #path('home/', views.home, name="home")
"""


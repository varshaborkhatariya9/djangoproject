from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('contact',views.contact,name="contact"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('changepassword',views.changepassword,name="changepassword"),
    path('forgetpassword',views.forgetpassword,name="forgetpassword"),
    path('otp',views.otp,name="otp"),
    path('newpassword',views.newpassword,name="newpassword"),
    path('profile',views.profile,name="profile")
    
]
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('profile/edit/',views.edit_profiles, name='edit_profile'),
    path('profile/edit/pass_change/', views.pass_change, name='pass_change'),
    path('change_pass/', views.change_pass, name='change_pass'),
]

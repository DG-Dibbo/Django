from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('signup/', views.register, name='register'),
    # path('login/', views.user_login, name='login'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    # path('logout/',views.LogoutView.as_view(), name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('profile/edit/',views.edit_profiles, name='edit_profile'),
    path('profile/edit/pass_change/', views.pass_change, name='pass_change'),
    path('change_pass/', views.change_pass, name='change_pass'),
]

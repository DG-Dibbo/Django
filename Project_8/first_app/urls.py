from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('changepassword/', views.pass_change, name='changepassword'),
    path('changepassword2/', views.pass_change2, name='changepassword2'),
    path('profile/', views.profile, name='profile'),
    # path('change_data/', views.user_change_data, name='user_change_data'),
    # add more patterns as needed
]

from django.urls import path
from . import views
urlpatterns = [
    path('',views.set_session,name='home'),
    path('get/',views.get_session,name='get_session'),
    path('del/',views.delete_session,name='delete_session'),
    # path('del/',views.delete_cookie,name='delete_cookie'),
]

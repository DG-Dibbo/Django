from django.urls import path
from . import views
from . forms import contactForm,studentForm,passwordform
urlpatterns = [
    path('about/',views.about,name = 'about'),
    path('form/',views.submit_form,name='submit_form'),
    path('djangoform/',views.DjangoForm,name='DjangoForm'),
    path('studentform/', views.Studentform, name='Studentform'),
    path('passwordfrom/', views.PasswordForm, name='PasswordForm'),
]

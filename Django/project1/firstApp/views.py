from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def courses(request):
    return HttpResponse("This is Courses Page.")

def about(request):
    return HttpResponse("This is about section. My name is Dibbo Ghosh")
def home(request):
    return HttpResponse("This is home page of firstApp")

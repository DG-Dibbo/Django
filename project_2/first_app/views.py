from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    # return HttpResponse("This is my home page")
    return render(request,'first_App/home.html')

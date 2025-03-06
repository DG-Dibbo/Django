from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("I am Home Gard")

def sum(request):
    summation = 2+4
    return HttpResponse(summation)

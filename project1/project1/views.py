from django.http import HttpResponse

def home(request):
    return HttpResponse("This is my home page")
def contact(request):
    return HttpResponse("This is my contact page")
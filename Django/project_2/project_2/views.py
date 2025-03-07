from django.shortcuts import render
from django.http import HttpResponse

# D:\Phitron Batch 4\My Personal Drive\Phitron batch 4\Django\project_2\templates
def index(request):
    return render(request,'index.html')

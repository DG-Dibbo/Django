from django.shortcuts import render
from posts.models import Post
# from django.http import HttpResponse
# Create your views here.

def homepage(request):
    data = Post.objects.all()
    # print(data)
    # for i in data:
    #     print(i.title)
    #     for j in i.category.all():
    #         print(j)
    return render(request,'index.html',{'data':data})

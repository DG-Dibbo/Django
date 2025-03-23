from django.shortcuts import render
from posts.models import Post
from categories.models import Category
# from django.http import HttpResponse
# Create your views here.

def homepage(request,category_slug = None):
    data = Post.objects.all()
    # print(data)
    # for i in data:
    #     print(i.title)
    #     for j in i.category.all():
    #         print(j)
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        data = Post.objects.filter(category = category)
    category = Category.objects.all()
    return render(request,'index.html',{'data':data,'category':category})

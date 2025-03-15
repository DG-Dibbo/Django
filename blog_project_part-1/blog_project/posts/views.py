from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.

def add_post(request):
    if request.method == 'POST':
        post_form = forms.PageForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')
    else:
        post_form = forms.PageForm()
    return render(request,'add_post.html',{'form':post_form})

def edit_post(request,id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PageForm(instance= post)
    print(post.title)
    if request.method == 'POST':
        post_form = forms.PageForm(request.POST,instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')
        
    return render(request,'add_post.html',{'form':post_form})

def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')

# def read_post(request,id):
#     post = models.Post.objects.get(pk=id)
#     return redirect('edit_post')   
    # return render(request,'add_post.html',{'form': post_form})

def read_post(request, id):
    post = models.Post.objects.get(pk=id)
    return render(request, 'read_post.html', {'post': post})

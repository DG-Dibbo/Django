from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from . import forms
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView,FormView
# Create your views here.

@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = forms.PageForm(request.POST,request.FILES)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('homepage')
    else:
        post_form = forms.PageForm()
    return render(request,'add_post.html',{'form':post_form})

#add post class based view
@method_decorator(login_required,name='dispatch')
class AddPostCreateView(CreateView):
    model = models.Post
    form_class = forms.PageForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('homepage')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@login_required
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

#edit post class based view
@method_decorator(login_required,name='dispatch')
class EditPostUpdateView(UpdateView):
    model = models.Post
    form_class = forms.PageForm
    template_name = 'add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

@login_required
def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')

# delete post class based view
@method_decorator(login_required,name='dispatch')
class DeletePostDeleteView(DeleteView):
    model = models.Post
    pk_url_kwarg = 'id'
    template_name = 'delete.html'
    success_url = reverse_lazy('homepage')

class PostDetailView(DetailView):
    model = models.Post
    template_name = 'post_detail.html'
    pk_url_kwarg = 'id'

    def post(self,request,*args,**kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    

# def read_post(request,id):
#     post = models.Post.objects.get(pk=id)
#     return redirect('edit_post')   
    # return render(request,'add_post.html',{'form': post_form})
@login_required
def read_post(request, id):
    post = models.Post.objects.get(pk=id)
    return render(request, 'read_post.html', {'post': post})

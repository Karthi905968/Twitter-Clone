from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import PostForm
# Create your views here.
def posts(request):

    if request.method=='POST':
        form=PostForm(request.POST , request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    
    posts=Post.objects.all().order_by('-created_at')

    return render(request,'post/post.html',{'post':posts})


def delete(request,post_id):
    posts=Post.objects.get(id=post_id)
    posts.delete()
    return HttpResponseRedirect('/')

def edit(request,post_id):
    post=Post.objects.get(id=post_id)
    return render(request,'post/update.html',{'post':post})


def update(request,post_id):
     post=Post.objects.get(id=post_id)
     form=PostForm(request.POST,request.FILES,instance=post)
     if form.is_valid():
        form.save()
        return HttpResponseRedirect('/') 
     else:
        return HttpResponseRedirect(form.errors.as_json())
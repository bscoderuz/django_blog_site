from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .models import Post
from .forms import PostForm


# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': "About Page"})


def post_detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)


def post_create(request):
    form = PostForm(data=request.POST)
    if form.is_valid():
        newdoc = form.save(commit=False)
        newdoc.author = request.user
        newdoc.save()
        return redirect('blog-home')
    return render(request, 'blog/post_form.html', {'form': form})



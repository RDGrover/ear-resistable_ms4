from django.shortcuts import render
from .models import BlogPost
# Create your views here.


def blog_list(request):
    posts = BlogPost.objects.all()

    context = {
        "posts": posts,
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request):
    model = BlogPost

    context = {
        "model": model,
    }

    return render(request, 'blog/blog_detail.html', context)

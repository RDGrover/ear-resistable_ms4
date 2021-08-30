from django.shortcuts import render
from .models import BlogPost
# Create your views here.


def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')

    return render(request, 'blog/blog.html', {"posts": posts})


def blog_detail(request):
    model = BlogPost

    return render(request, 'blog/blog_detail.html', {"model": model})

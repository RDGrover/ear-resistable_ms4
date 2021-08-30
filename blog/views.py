from django.shortcuts import render
from .models import BlogPost
# Create your views here.


def blog_list(request):
    posts = list(BlogPost.objects.all())

    context = {
        "posts": posts,
    }
    print(blog_list)
    return render(request, 'blog/blog.html', context)


def blog_detail(request, post_id):
    model = BlogPost

    context = {
        "model": model,
    }

    return render(request, 'blog/blog_detail.html', context)

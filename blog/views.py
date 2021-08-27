from django.shortcuts import render
from .models import BlogPost, Comments
# Create your views here.


def blog_list(request):
    posts = BlogPost.objects.all().limit(5)

    return render(request, 'blog/blog.html', {"posts": posts})

# def blog_detail():


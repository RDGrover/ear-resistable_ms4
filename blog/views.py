from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from .forms import CommentsForm


def blog_list(request):
    posts = list(BlogPost.objects.all())

    context = {
        "posts": posts,
    }
    print(blog_list)
    return render(request, 'blog/blog.html', context)


def blog_detail(request, post_id):
    model = BlogPost
    post = get_object_or_404(BlogPost, id=post_id)
    new_comment = None

    if request.method == 'POST':
        comments_form = CommentsForm(data=request.POST)
        if comments_form.is_valid():
            new_comment = comments_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comments_form = CommentsForm()

    context = {
        "model": model,
        "post": post,
        "new_comment": new_comment,
        "comments_form": comments_form,
    }

    return render(request, 'blog/blog_detail.html', context)

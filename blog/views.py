from django.shortcuts import render

from blog.models import Post


def all_posts(request, author=None):
    if author:
        posts = Post.objects.filter(author=author)
    else:
        posts = Post.objects.all()
    return render(context={'posts': posts},
                  template_name='blog/index.html',
                  request=request)

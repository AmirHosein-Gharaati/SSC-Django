from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
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


def new_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if not request.user.is_authenticated:
            author = request.POST.get('author')
        else:
            author = request.user.username
        post = Post(title=title, content=content, author=author)
        post.save()
        return HttpResponseRedirect('/blogs')

    return render(request, 'blog/new_post.html')

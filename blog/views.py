from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from blog.models import Post


def all_posts(request, author=None):
    if author:
        posts = Post.objects.filter(author=author)
    else:
        posts = Post.objects.all()
    return render(context={'posts': posts},
                  template_name='blog/index.html',
                  request=request)


class NewPost(View):
    def get(self, request):
        return render(request, 'blog/new_post.html')

    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        if not request.user.is_authenticated:
            author = request.POST.get('author')
        else:
            author = request.user.username
        post = Post(title=title, content=content, author=author)
        post.save()
        messages.add_message(request, messages.INFO, "CREATED THANK YOU")

        return HttpResponseRedirect('/blogs')


class AllPosts(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        author = self.kwargs.get('author')
        return Post.objects.all() if not author else Post.objects.filter(author=author)
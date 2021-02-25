from django.http import HttpResponse
from django.template import loader

from blog.models import Post


def all_posts(request):
    template = loader.get_template('blog/index.html')
    posts = Post.objects.all()
    content = template.render(context={'posts': posts}, request=request)
    return HttpResponse(content=content)

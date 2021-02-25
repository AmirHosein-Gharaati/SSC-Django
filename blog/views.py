from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('blog/index.html')
    content = template.render({}, request)
    return HttpResponse(content=content)

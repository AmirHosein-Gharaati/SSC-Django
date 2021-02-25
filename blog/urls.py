from django.urls import path

from blog.views import all_posts

urlpatterns = [
    path('', all_posts, name='all_posts'),
    path('<author>', all_posts, name='author_posts')
]

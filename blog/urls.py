from django.contrib.auth.views import LoginView
from django.urls import path, reverse

from blog.views import all_posts, new_post

urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('new_post/', new_post, name='new_post'),
    path('<author>/', all_posts, name='author_posts'),
    path('', all_posts, name='all_posts'),
]

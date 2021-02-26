from django.contrib.auth.views import LoginView
from django.urls import path

from blog.views import NewPost, AllPosts

urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('new_post/', NewPost.as_view(), name='new_post'),
    path('<author>/', AllPosts.as_view(), name='author_posts'),
    path('', AllPosts.as_view(), name='all_posts'),
]

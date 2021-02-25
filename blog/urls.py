from django.urls import path

from blog.views import all_posts

urlpatterns = [
    path('', all_posts)
]

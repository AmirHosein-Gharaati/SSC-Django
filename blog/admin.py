from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('author',)
    list_display = ('title', 'author', 'created_at')

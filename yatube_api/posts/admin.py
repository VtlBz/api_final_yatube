from django.contrib import admin

from .models import Comment, Follow, Group, Post

DEFAULT_FOR_EMPTY: str = '-пусто-'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group',)
    list_editable = ('group',)
    search_fields = ('text', 'author',)
    list_filter = ('pub_date',)
    empty_value_display = DEFAULT_FOR_EMPTY


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description',)
    search_fields = ('title', 'description', 'slug',)
    list_filter = ('title',)
    empty_value_display = DEFAULT_FOR_EMPTY


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'created', 'author', 'post',)
    search_fields = ('text', 'author', 'post',)
    list_filter = ('created',)
    empty_value_display = DEFAULT_FOR_EMPTY


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'following',)
    search_fields = ('user', 'following',)
    list_filter = ('user', 'following',)
    empty_value_display = DEFAULT_FOR_EMPTY

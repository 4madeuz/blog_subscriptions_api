from django.contrib import admin

from .models import Post, Blog, Subscription, UserFeed


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'id'
    )


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'updated_at',
        'created_at',
        'blog',
        'text',
    )
    search_fields = ('blog__user',)


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'subscriber',
        'blog',
        'id'
    )


class NewsFeedAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'id',
    )


admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(UserFeed, NewsFeedAdmin)

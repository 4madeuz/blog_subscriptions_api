from django.contrib import admin

from .models import Post, Blog, Subscription


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'user',
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
    )


admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Subscription, SubscriptionAdmin)

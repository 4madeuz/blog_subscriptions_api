from rest_framework import serializers
from blog.models import Post, Subscription, UserFeed
from django.core.paginator import Paginator


class PostViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'text', 'title', 'blog']


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['text', 'title']


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['subscriber', 'blog']


class UserFeedSerializer(serializers.ModelSerializer):

    posts = serializers.SerializerMethodField('paginated_posts')

    class Meta:
        model = UserFeed
        fields = ['user', 'posts', 'read_posts']

    def paginated_posts(self, obj):
        page_size = self.context['request'].query_params.get('size') or 10
        paginator = Paginator(obj.posts.all(), page_size)
        page = self.context['request'].query_params.get('page') or 1

        posts = paginator.page(page)
        serializer = PostViewSerializer(posts, many=True)

        return serializer.data

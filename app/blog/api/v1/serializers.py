from rest_framework import serializers
from blog.models import Post, Subscription


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['text', 'title']


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['subscriber', 'blog']

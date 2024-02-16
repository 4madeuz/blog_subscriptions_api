from blog.api.v1.serializers import PostSerializer, SubscriptionSerializer
from rest_framework import status, viewsets


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer

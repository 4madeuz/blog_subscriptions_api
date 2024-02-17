from blog.api.v1.serializers import PostCreateSerializer, SubscriptionSerializer, UserFeedSerializer, PostViewSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from blog.models import Post, Subscription, UserFeed
from blog.permissions import IsOwnerOrAdminPermission
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .services import refresh_feed


class UserFeedPagination(PageNumberPagination):
    page_size = 10


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def get_permissions(self):
        if self.action == 'get':
            return [AllowAny()]
        elif self.action == 'create':
            return [IsAuthenticated()]
        else:
            return [IsOwnerOrAdminPermission()]

    def perform_create(self, serializer):
        serializer.save(blog=self.request.user.blog)


class SubscriptionViewSet(viewsets.mixins.CreateModelMixin,
                          viewsets.mixins.DestroyModelMixin,
                          viewsets.mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return Subscription.objects.filter(subscriber=self.request.user.id)


class UserFeedViewSet(viewsets.mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = UserFeedSerializer
    pagination_class = UserFeedPagination
    permission_classes = [IsAuthenticated,]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'size',
                openapi.IN_QUERY,
                description='Amount of posts per page',
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                'page',
                openapi.IN_QUERY,
                description='Number of page',
                type=openapi.TYPE_STRING,
            ),
        ]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def get_object(self):
        feed = get_object_or_404(UserFeed, user=self.request.user.id)
        refresh_feed(feed)
        return feed

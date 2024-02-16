from blog.api.v1.serializers import PostSerializer, SubscriptionSerializer
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from blog.models import Post, Subscription
from blog.permissions import IsOwnerOrAdminPermission


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

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
        return Subscription.objects.filter(subscriber=self.request.user)

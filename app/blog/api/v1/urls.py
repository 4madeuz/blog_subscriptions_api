from rest_framework.routers import DefaultRouter
from .views import PostViewSet, SubscriptionViewSet, UserFeedViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'subscriptions', SubscriptionViewSet, basename='subscription')
router.register(r'newsfeed', UserFeedViewSet, basename='newsfeed')

urlpatterns = router.urls

from rest_framework.routers import DefaultRouter
from .views import PostViewSet, SubscriptionViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'subscriptions', SubscriptionViewSet, basename='subscription')

urlpatterns = router.urls

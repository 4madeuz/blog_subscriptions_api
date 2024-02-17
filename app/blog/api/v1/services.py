from blog.models import UserFeed, Post


def refresh_feed(user_feed: UserFeed) -> None:
    subscribed_blogs = user_feed.user.subscriptions.all()

    latest_posts = Post.objects.filter(blog__in=subscribed_blogs.values_list('blog', flat=True)).order_by('-created_at')[:500]

    user_feed.posts.set(latest_posts)
    user_feed.save()

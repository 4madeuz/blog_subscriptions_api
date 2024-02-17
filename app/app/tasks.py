from celery import shared_task
from celery.utils.log import get_task_logger
from django.contrib.auth import get_user_model
from blog.models import UserFeed

logger = get_task_logger(__name__)


User = get_user_model()

@shared_task
def send_latest_posts_to_users():
    # Fetch all users
    users = User.objects.all()

    for user in users:
        try:
            user_feed = UserFeed.objects.get(user=user)
            latest_posts = user_feed.posts.all().order_by('-created_at')[:5]

            # Print or process the posts as needed
            for post in latest_posts:
                print(f"User: {user.username}, Post Title: {post.title}, Created At: {post.created_at}")

        except UserFeed.DoesNotExist:
            # Handle the case where the user does not have a UserFeed
            print(f"User: {user.username} does not have a UserFeed.")

    return "Latest posts sent to all users."

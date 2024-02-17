from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from blog.models import Blog, UserFeed

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_blog(sender, instance, created, **kwargs):
    if created:
        blog = Blog(user=instance)
        blog.save()


@receiver(post_save, sender=User)
def create_user_newsfeed(sender, instance, created, **kwargs):
    if created:
        blog = UserFeed(user=instance)
        blog.save()

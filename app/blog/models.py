import uuid

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField('created', auto_now_add=True)
    updated_at = models.DateTimeField('updated', auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Blog(UUIDMixin, TimeStampedMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user} blog'

    class Meta:
        db_table = 'content"."blogs'


class Post(UUIDMixin, TimeStampedMixin):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(blank=False, max_length=50)
    text = models.CharField(max_length=140)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'content"."posts'


class Subscription(UUIDMixin, TimeStampedMixin):
    subscriber = models.ForeignKey(User, related_name='subscriptions', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.subscriber}/{self.blog}'

    class Meta:
        db_table = 'content"."subscriptions'
        constraints = [
                models.UniqueConstraint(
                    fields=['subscriber', 'blog'], name='subscriber_blog_constraint'
                )
            ]


class UserFeed(UUIDMixin, TimeStampedMixin):
    user = models.ForeignKey(User, related_name='user_feed', on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post, related_name='user_feed')
    read_posts = models.ManyToManyField(Post, related_name='read_posts', blank=True)

    class Meta:
        db_table = 'content"."newsfeeds'

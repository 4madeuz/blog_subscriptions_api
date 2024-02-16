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

    class Meta:
        db_table = 'content"."blogs'


class Post(UUIDMixin, TimeStampedMixin):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(blank=False, max_length=50)
    text = models.CharField(max_length=140)

    class Meta:
        db_table = 'content"."posts'


class Subscription(UUIDMixin, TimeStampedMixin):
    subscriber = models.ForeignKey(User, related_name='subscriptions', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        db_table = 'content"."subscriptions'

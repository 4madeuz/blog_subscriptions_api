from celery import shared_task
from celery.utils.log import get_task_logger
from django.utils import timezone

logger = get_task_logger(__name__)


@shared_task
def send_selected_posts():
    pass

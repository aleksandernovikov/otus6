from datetime import timedelta

import pytz
from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Lesson


@receiver(pre_save, sender=Lesson)
def fill_display_name(sender, instance, **kwargs):
    """
    Время окончания урока - добавим 45 к времени начала урока, будем засорять БД
    """
    if not instance.id and not instance.end_time:
        timezone = pytz.timezone(settings.TIME_ZONE)
        end_time = instance.start_time + timedelta(minutes=45)
        instance.end_time = end_time.astimezone(timezone)

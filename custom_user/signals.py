from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import UniversityUser


@receiver(pre_save, sender=UniversityUser)
def fill_display_name(sender, instance, **kwargs):
    if not instance.id and not instance.display_name:
        instance.display_name = f'{instance.first_name} {instance.middle_name} {instance.last_name}'.strip()

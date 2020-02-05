from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models


class UniversityUser(AbstractUser):
    middle_name = models.CharField(_('Middle Name'), max_length=100)
    display_name = models.CharField(_('Display name'), max_length=150, blank=True, null=True)

    def __str__(self):
        return self.display_name if self.display_name else self.username

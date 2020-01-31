from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models


class UniversityUser(AbstractUser):
    middle_name = models.CharField(_('Middle Name'), max_length=100)

    def get_full_name(self):
        """
        Полное ФИО
        """
        return f'{self.first_name} {self.middle_name} {self.last_name}'.strip()

from django.contrib import admin

from custom_user.models import UniversityUser


@admin.register(UniversityUser)
class UniversityUserAdmin(admin.ModelAdmin):
    pass

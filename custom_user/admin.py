from django.contrib import admin

from custom_user.models import UniversityUser


@admin.register(UniversityUser)
class UniversityUserAdmin(admin.ModelAdmin):
    search_fields = ('username', 'first_name', 'middle_name', 'last_name', 'display_name')
    ordering = ('id',)
